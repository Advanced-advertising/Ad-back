#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

pip install -r requirements.txt
python manage.py migrate --noinput

if [ "$MODE" = "PRODUCTION" ] || [ "$MODE" = "STAGING" ]
then
  cp -rf media/* media/
  cp -rf static/* static/
  python manage.py collectstatic --noinput
  gunicorn adBack.wsgi:application --worker-class=gevent --worker-connections=1000 --workers=5 --bind 0.0.0.0:8000
else
  exec "$@"
fi

exec "$@"
