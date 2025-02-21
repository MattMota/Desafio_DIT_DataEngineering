#!/bin/bash
set -e

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  echo "PostgreSQL is unavailable - waiting"
  sleep 2
done

echo "PostgreSQL is up, starting Prefect"
exec "$@"
