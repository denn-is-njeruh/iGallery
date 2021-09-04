SHELL := /bin/bash

include .env

install:
	pipenv install

activate:
	pipenv shell

run:
	python3 manage.py runserver

migration:
	python manage.py makemigrations

migrate:
	python3 manage.py migrate

superuser:
	python3 manage.py createsuperuser

heroku:
	git push heroku migration

deploy:
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

