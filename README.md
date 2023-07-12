*** Clonar el repositorio ***

En una carpeta de su preferencia, clonar el repositorio con el siguiente comando:
```
git clone #http del repositorio
```

*** Para instalar el proyecto ***

```
py -m venv venv   o   python -m venv venv
venv\Scripts\activate
```
*** instalar las dependencias ***
```
pip install -r requirements.txt
```
*** Para crear la base de datos ***
```
Hacer un archivo en la carpeta Settings llamado local.py y agregar lo que dice en el archivo base.py respecto de la base de datos
```
*** Para crear las migraciones ***
```
python manage.py makemigrations
python manage.py migrate
```

*** Para ejecutar el proyecto ***
```
python manage.py runserver
``