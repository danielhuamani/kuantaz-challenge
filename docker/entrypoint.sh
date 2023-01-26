#!/usr/bin/env bash
echo "Starting server"
sleep 5
exec "$@"
flask db init
flask db migrate
flask db upgrade
python src/flask_app.py