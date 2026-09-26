import os

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_default_superuser(sender, **kwargs):
    """Create an admin user only when credentials are supplied via environment variables."""
    from django.contrib.auth import get_user_model

    username = os.getenv("DJANGO_ADMIN_USERNAME")
    email = os.getenv("DJANGO_ADMIN_EMAIL")
    password = os.getenv("DJANGO_ADMIN_PASSWORD")

    if not all([username, email, password]):
        return

    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)


class ReservationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reservations"

    def ready(self):
        post_migrate.connect(create_default_superuser, sender=self)
