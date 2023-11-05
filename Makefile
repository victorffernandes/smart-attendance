


setup:
	docker run --name smartdb -p 3306:3306 -e MYSQL_USER=mysql_user -e MYSQL_DATABASE=smartdb -e MYSQL_PASSWORD=priv4te -e MYSQL_ALLOW_EMPTY_PASSWORD=true -d mysql

start:
	docker start smartdb
	python app/manage.py runserver 0.0.0.0:80

test:
  docker start smartdb
  python app/manage.py test smartattendance -v 2
