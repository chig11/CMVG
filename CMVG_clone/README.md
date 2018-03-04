# CMVG

Follow this link to install and run django apps https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04

Follow this link to install Postgresql
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04

command for postgresql port:
  - sudo netstat -plunt | grep postgres

heroku
  - pip install -r requirements.txt 
  - pip install dj-database-url gunicorn psycopg2 whitenoise

other postgresql cmd
  - sudo su postgres
  - psql
  - CREATE DATABASE django;
  - ALTER USER postgres WITH PASSWORD 'test1234';
  - \l
  - \du
  - \q

django commands
  - python manage.py runserver
  - python manage.py createsuperuser
  - python manage.py loaddata courses.json

heroku
https://www.youtube.com/watch?v=2kvTsCskJA0

  - python manage.py migrate (every pull a git)
  - python manage.py createsuperuser
  - python manage.py runserver (run the app)
  
 git commands
  - git pull (every time)