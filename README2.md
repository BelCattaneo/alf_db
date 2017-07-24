1. `Crear usuario en https://bitbucket.org`
2. `Abrir la terminal (Konsole)`
3. `Instalar Git: sudo apt-get install git`
4. `Clonar repositorio de Bit Bucket: git clone Link (el link se copia de la foto_1)`
5. `Entrar a la carpeta del proyecto: cd alf_db (A partir de este paso siempre se debe trabajar desde este directorio)`
6. `Instalar la base de datos: sudo apt-get install postgresql postgresql-contrib`
7. `Cambiar de usuario a posgres (base de datos): sudo su postgres (foto_2)`
8. `Entrar a el cliente de la base de datos: psql (foto_2)`
9. `Crear usuario (no olvidar el punto y coma al final): create user admin with password 'admin'; (foto_2)`
10. `Crear base de datos (no olvidar el punto y coma al final): create database alf with owner = admin; (foto_2)`
11. `Salir del cliente tipeando: \q (foto_2)`
12. `Salir del usuario postgres tipeando: exit (foto_2)`
13. `Instalar Python 3 (Puede que ya esté instalado): sudo apt-get install python3`
14. `Descargar pip (pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python): wget https://bootstrap.pypa.io/get-pip.py`
15. `Instalar pip: sudo python3 get-pip.py`
16. `Instalar dependencias del Sistema operativo para poder programar sobre Python y Postgres: sudo apt-get install python-pip python-dev libpq-dev`
17. `Instalar Virtualenv (Virtualenv permite tener diferentes proyectos con diferentes versiones de dependencias): sudo pip install virtualenv`
18. `Crear un ambiente virtual: virtualenv alf_env`
19. `Activar el ambiente virtual: source alf_env/bin/activate (se debe mostrar adelante: (alf_env))`
20. `Instalar librerias necesarias: pip install -r requirements.txt`
21. `Correr las migraciones para generar las tablas en la base de datos: python manage.py migrate`
22. `Correr el programa: python manage.py runserver`
23. `En Chrome entrar a: http://localhost:8000`