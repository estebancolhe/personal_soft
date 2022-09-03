# Prueba tecnica personal soft

Implementar una solución que permita realizar un CRUD sobre la información de libros.

## Run

Luego de clonar el repositorio, se utilizara la terminal para instalar librerías, realizar migraciones y ejecutar la aplicación:

Para instalar librerías se utilizara el comando:

```terminal
pip install -r requirements.txt
```
Para ejecutar la aplicación se requiere el comando:
```terminal
python manage.py runserver
```
## Endpoints
En el repositorio se encuentra un archivo llamado endpoints.json el cual es un archivo exportado desde postman con todos los endpoints que posee la prueba, este archivo se puede importar nuevamente en postman para leer de mejor manera los endpoints que se deben utilizar.

## Antes de comenzar
Es importante aclarar que la prueba tecnica cuenta con permisos para usuarios, un usuario basico puede listar, crear y actualizar información pero no puede eliminarla, el usuario que puede realizar todas estas acciones es un usuario admin, a continuacion pondré las credenciales de acceso de cada usuario.

1. usuario basico
. email:andres.p@gmail.com
. password:123456

2. usuario admin
. email:esteban.h@gmail.com
. password:123456

## Acciones posibles

En la API se pueden realizar las siguientes acciones, registro de usuarios, login y logout, CRUD de los libros, ademas la API cuenta con un logger el cual registra en la tabla 'logs' los endpoints utilizados por cada usuario.

## Autenticacion

Cuando un usuario realiza login, la API devuelve el token, este token debe enviarse como un header en los endpoints de CRUD para libros y CRUD para actionTypes.

## Logger

El logger registra todo lo que un usuario hace en la API, la tabla de logs tiene una FK que indica el ID de la accion realizada, esta FK se llama actionType y la API permite agregar, listar, editar y borrar actionsType como desee.




