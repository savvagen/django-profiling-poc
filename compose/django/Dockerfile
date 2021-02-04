FROM python:3.7-slim-stretch

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y libpq-dev python-dev gcc

RUN addgroup --system django && adduser --system --ingroup django django

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY /compose/django/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /gunicorn.sh
RUN chown django /gunicorn.sh

COPY /compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown django /entrypoint.sh

COPY . /app
RUN chown -R django /app

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
