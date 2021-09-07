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
	python3 manage.py createsuperuser

test:
	python3 manage.py test

heroku:
	git push heroku migration

deploy:
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

