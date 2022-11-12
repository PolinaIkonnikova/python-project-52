install:
	poetry install

uninstall:
	python3 -m pip uninstall hexlet-code

lint:
	poetry run flake8 task_manager

test:
	python manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml
	poetry run coverage report

req:
	poetry export -f requirements.txt -o requirements.txt
