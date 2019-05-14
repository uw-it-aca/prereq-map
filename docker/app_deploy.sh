source "/app/bin/activate"

cd /app
python manage.py loaddata curric_titles.json
