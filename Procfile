release: python manage.py migrate
web: gunicorn hotel_api.wsgi --bind 0.0.0.0:$PORT --timeout 120 --log-file -
