### Development Guide
1. `sudo apt-get install python3`
2. `udo apt-get install git`
3. `git clone https://github.com/BelCattaneo/alf_db.git`
4. `wget https://bootstrap.pypa.io/get-pip.py`
5. `sudo python3 get-pip.py`
6. `pip install --user virtualenv`

> From project's root folder

7. `virtualenv alf_env`
8. `source alf_env/bin/activate`
9. `pip install -r requirements.txt`

> Create user and database for project

10. `psql create user admin with password 'admin';`
11. `psql create database alf with owner = admin;`

> Run migrations

12. `python manage.py migrate`

> Run app
13. `python manage.py runserver`

> Database

Drop all tables in alf_db => `python manage.py sqlflush | python manage.py dbshell`
Seed info to database => `python manage.py loaddata data.json`


