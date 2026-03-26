from django.apps import AppConfig


class ReservationsConfig(AppConfig):
    name = 'reservations'


from django.contrib.auth import get_user_model

class ReservationsConfig(AppConfig):
    ...

    def ready(self):
        User = get_user_model()

        try:
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    "admin",
                    "admin@example.com",
                    "admin123"
                )
        except Exception:
            pass