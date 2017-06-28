### Development Guide

1. `git clone git@github.com:BelCattaneo/alf_db.git`
2. `get https://bootstrap.pypa.io/get-pip.py`
3. `sudo python3 ~/get-pip.py`
4. `pip install --user virtualenv`

> From project's root folder

5. `virtualenv alf_env`
6. `source alf_env/bin/activate`
7. `pip install -r requirements.txt`

> Create user and database for project

8. `create user admin with password 'admin';`
9. `create database alf with owner = admin;`

> Run migrations

10. `python manage.py migrate`

> Database

Drop all tables in alf_db => `python manage.py sqlflush | python manage.py dbshell`
Seed info to database => `python manage.py loaddata data.json`


