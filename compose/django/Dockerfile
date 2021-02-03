FROM python:3.7.7-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
  && apk add --no-cache bash \
  # psycopg2 dependencies
  && apk add --virtual build-deps g++ gcc  python3-dev musl-dev libevent-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Paramiko dependecies
  && apk add make \
  # PythonLDAP
  && apk add openldap-dev \
  && apk add curl

RUN addgroup -S django && adduser -S -G django django

# Install requirements
RUN pip install --upgrade pip setuptools wheel
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r ./app/requirements.txt


COPY ./compose/django/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /gunicorn.sh
RUN chown django /gunicorn.sh

COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown django /entrypoint.sh


COPY . /app
RUN chown -R django /app

RUN mkdir -p /app/media && chown -R django /app/media

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
