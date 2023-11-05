sleep 20
python app/manage.py migrate
python app/manage.py loaddata app/smartattendance/fixtures/initial_data.json
python app/manage.py runserver 0.0.0.0:80