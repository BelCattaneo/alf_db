Manual de Instalación

1) Crear usuario en https://bitbucket.org
2) Abrir la terminal (Konsole)
3) Instalar Git: 
	sudo apt-get install git
4) Clonar repositorio de Bit Bucket: 
	git clone [Link] (el link se copia de la foto_1)
5) Entrar a la carpeta del proyecto: 
	cd alf_db (A partir de este paso siempre se debe trabajar desde este directorio)
6) Instalar la base de datos: 
	sudo apt-get install postgresql postgresql-contrib
7) Cambiar de usuario a posgres (base de datos):
	sudo su postgres (foto_2)
8) Entrar a el cliente de la base de datos: 
	psql (foto_2)
9) Crear usuario (no olvidar el punto y coma al final): 
	create user admin with password 'admin'; (foto_2)
10)  Crear base de datos (no olvidar el punto y coma al final): 
	create database alf with owner = admin; (foto_2)
11)  Salir del cliente tipeando:
	\q (foto_2)
12)  Salir del usuario postgres tipeando: 
	exit (foto_2)
13)  Instalar Python 3 (Puede que ya esté instalado):
	sudo apt-get install python3
14)  Descargar pip (pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python): 
	wget https://bootstrap.pypa.io/get-pip.py
15)  Instalar pip:
	sudo python3 get-pip.py
16)  Instalar dependencias del Sistema operativo para poder programar sobre Python y Postgres:
	sudo apt-get install python-pip python-dev libpq-dev
17)  Instalar Virtualenv (Virtualenv permite tener diferentes proyectos con diferentes versiones de dependencias):
	sudo pip install virtualenv
18)  Crear un ambiente virtual:
	virtualenv alf_env
19)  Activar el ambiente virtual:
	source alf_env/bin/activate (se debe mostrar adelante: (alf_env))
20)  Instalar librerias necesarias:
	pip install -r requirements.txt
21)  Correr las migraciones para generar las tablas en la base de datos
	python manage.py migrate
22)  Recolectar archivos estáticos:
	./manage.py collectstatic
23)  Instalar el sistema de control y monitoreo de Cliente/Servidor:
	sudo apt-get install supervisor
24)  Copiar el documento "gunicorn_start" en la carpeta /bin:
	sudo cp [carpeta de destino] /bin
25)  Convertir el archivo en un ejecutable:
	sudo chmod +x /bin/gunicorn_start
26)  Instalar nginx:
	sudo apt-get install nginx
27)  Copiar el documento "alf" en la carpeta /etc/nginx/sites-available:
	sudo cp [carpeta de destino] /etc/nginx/sites-available
28)  Chequear sintaxis del archivo nginx:
	sudo nginx -t
29)  Generión de acceso directo al documento alf para que el mismo este habilitado:
	sudo ln -s /etc/nginx/sites-available/alf /etc/nginx/sites-enabled
30)  Se reinicia nginx:
	sudo service nginx restart
31)  Generación del archivo de configuración:
	Copiar el archivo alf.conf en /etc/supervisor/conf.d/
32)  Releer el archivo de configuración:
	sudo supervisorctl reread
33) Actualizar el archivo de configuración
	sudo supervisorctl update 
34)  Iniciar la aplicación:
	sudo supervisorctl start alf

