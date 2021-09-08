SHELL: #!/bin/bash

shell:
	python manage.py shell
	
run:
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python3 manage.py createsuperuser --username ${name}

test:
	python3 manage.py test

heroku:
	git push heroku migration

collectstatic:
	python manage.py collectstatic

