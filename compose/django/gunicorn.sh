#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

cd src
python manage.py collectstatic --no-input --clear
python manage.py migrate

if [[ -n "$DJANGO_ADMIN_USERNAME" ]]; then
    echo "==> Creating super user"
    # create superuser
python manage.py shell << END
from django.contrib.auth.models import User
if not User.objects.filter(username='${DJANGO_ADMIN_USERNAME}').exists():
    User.objects.create_superuser('${DJANGO_ADMIN_USERNAME}', email='${DJANGO_ADMIN_EMAIL}', password='${DJANGO_ADMIN_PASSWORD}')
else:
    print('Superuser already exists')
END
fi


/usr/local/bin/gunicorn djangoprofiling.wsgi:application --bind=0.0.0.0:5000

/usr/local/bin/gunicorn --check-config
