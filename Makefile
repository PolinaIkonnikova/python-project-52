install:
	poetry install

uninstall:
	python3 -m pip uninstall hexlet-code

lint:
	poetry run flake8 task_manager

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml
	poetry run coverage report

req:
	poetry export -f requirements.txt -o requirements.txt

mess:
	python manage.py makemessages -l ru

compil:
	python manage.py compilemessages

server:
	python manage.py runserver
