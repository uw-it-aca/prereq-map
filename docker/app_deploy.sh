source "/app/bin/activate"

cd /app
python manage.py migrate
python manage.py clear_data
python manage.py loaddata curric_titles.json
python manage.py loaddata course_titles.json
