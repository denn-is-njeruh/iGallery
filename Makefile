SHELL := /bin/bash

include .env

install:
	pipenv install

activate:
	pipenv shell

shell:
	python manage.py shell
	
run:
	python3 manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python3 manage.py migrate

superuser:
	python3 manage.py createsuperuser --username ${name}

test:
	python3 manage.py test

heroku:
	git push heroku migration

collectstatic:
	python manage.py collectstatic

