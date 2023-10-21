


setup:
	docker run --name smartdb -p 3306:3306 -e MYSQL_USER=mysql_user -e MYSQL_DATABASE=smartdb -e MYSQL_PASSWORD=priv4te -e MYSQL_ALLOW_EMPTY_PASSWORD=true -d mysql

start:
	python app/manage.py migrate
	python app/manage.py runserver 0.0.0.0:8000

