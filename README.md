### Development Guide
1. `sudo apt-get install python3`
2. `sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib nginx`
3. `sudo nano /etc/init/gunicorn.conf`
4. `pegar
    
        description "Gunicorn application server handling alf_db"

        start on runlevel [2345]
        stop on runlevel [!2345]

        respawn
        setuid user
        setgid www-data
        chdir /home/user/Projects/alf

        exec alf_env/bin/gunicorn --workers 3 --bind unix:/home/user/Projects/alf.sock  alf.wsgi:application
    `
5.  `Ctrl + X para salir`
6. `tipear 'y' para guardar y enter`
7. `sudo apt-get install git`
8. `git clone https://github.com/BelCattaneo/alf_db.git`
9. `cd alf_db`
10. `wget https://bootstrap.pypa.io/get-pip.py`
11. `sudo python3 get-pip.py`
12. `pip install --user virtualenv`

> From project's root folder

8. `virtualenv alf_env`
9. `source alf_env/bin/activate`
10. `pip install -r requirements.txt`

> Create user and database for project
11. `sudo su postgres`
12. `psql`
13. `create user admin with password 'admin';`
14. `create database alf with owner = admin;`

> Run migrations

15. `python manage.py migrate`

> Run app
16. `python manage.py runserver`

> Database

Drop all tables in alf_db => `python manage.py sqlflush | python manage.py dbshell`
Seed info to database => `python manage.py loaddata data.json`


