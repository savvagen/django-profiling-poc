#!/bin/bash

if [ -z "${POSTGRES_USER}" ]; then
    # the official postgres image uses 'postgres' as default user if not set explictly.
    export POSTGRES_USER=postgres
fi
if [ -z "${POSTGRES_HOST}" ]; then
    export POSTGRES_HOST=postgres
fi

export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:5432/${POSTGRES_DB}"

postgres_is_ready(){
  python << END
import sys

import psycopg2

try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}"
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}

echo "Connecting to Postgres = postgres://${POSTGRES_USER}:*******@${POSTGRES_HOST}:5432/${POSTGRES_DB}"
until postgres_is_ready; do
  echo "Postgres is unavailable (sleeping)..."
  sleep 1
done
echo "Postgres is up - continuing..."


exec "$@"