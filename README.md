Consulta ciudadana
==================

API creada por José Emanuel Castelán a manera de ejercicio de conocimientos del framework "Django REST Framework", así como el modelo "twelve-app factor".

La intensión es emular un entorno de consulta de interés público en el gobierno actual.

## Instalación de la api ##

Para probar la app, es necesario correr uno de los entornos (suponiendo que se tiene instalado "docker" y "docker-compose")

- `local.yml` : Entorno de desarrollo. Correra en el host {{ip}}:8000
- `production.yml` : Entorno de producción. Correra en el host {{ip}}:80

Se debe procurar que en la carpeta de entorno deseado esten cargadas las variables de entornos

> vi .envs/.local/.sys

``````
DEBUG=on
DJANGO_SETTINGS_MODULE=consulta_ciudadana.settings.local

#Postgres
POSTGRES_USER=ingkstr
POSTGRES_PASSWORD=abcd1234
POSTGRES_HOST=dbcc
POSTGRES_PORT=5432
POSTGRES_DB=dbsys

# Redis
REDIS_URL=redis://redis:6379/0

# Flower
CELERY_FLOWER_USER=abcd
CELERY_FLOWER_PASSWORD=1234
``````

> vi .envs/.production/.sys

``````
DEBUG=off
DJANGO_SETTINGS_MODULE=consulta_ciudadana.settings.production

#Postgres
POSTGRES_USER=kjhjkdfjkshfsjdfiowjfuiewhiow786f34fiy487fh2f78
POSTGRES_PASSWORD=8734738fh89d7489jj4987rdj89ry932jj
POSTGRES_HOST=dbcc
POSTGRES_PORT=5432
POSTGRES_DB=dbsys

# Redis
REDIS_URL=redis://redis:6379/0

# Flower
CELERY_FLOWER_USER=hguhhf7824ueif2437rdh2uei
CELERY_FLOWER_PASSWORD=7894578934fu73879847t8934ht985h4

``````


Los siguientes comandos ejecutan la API.

> docker-compose -f <entorno>.yml build

> docker-compose -f <entorno>.yml run --rm django python manage.py makamigrations

> docker-compose -f <entorno>.yml up

En el primer arranque, se debe hacer un usuario staff

> docker-compose -f <entorno>.yml run --rm django python manage.py createsuperuser

## Descripción de la API ##

La API maneja tres usuarios

- `Staff` : El staff tiene privilegios de crear encueestas, dar de alta votantes y usuarios. También puede ver reportes de consultas finalizadas
- `Jefe de consulta` : Este actor habilita a un votante para acceder a una encuesta activa.
- `Nodo de voto` : El votante usa esta sesión para contestar una consulta.

## Funciones de administrador ##

La administración se realiza vía browser mediante el admin

 - `https://{{host}}/admin` : Usuarios staff se autentican

Existen 3 menus:

- `Polls` : Creación de encuestas. Pueden llevar hasta 10 preguntas del tipo "SI/NO" y no se pueden eliminar. Para que una encuesta ya se considere lista para publicar, se debe ejecutar la acción `set poll as ready`. Después de esto, la encuesta será pública en el periodo de duración y ya no podrá ser modificada.

- `Users` : Creación de usuarios. Ahí se definen si tiene privilegios staff, jefe de consulta (chief) o nodo de votación (node)

- `Voter` : Se carga la información del electorado que contestará las encueestas.

## Funciones de la API ##

Aún esta pendiente la documentación mediante "swagger".

-  `POST {{host}}/access/login` : Se envía por JSON username y password. Este regresa la información del usuario y un token que usara para autenticarse en las otras funciones
-  `GET {{host}}/voter/{{cid}}/poll` : Un usuario del tipo chief. Obtiene la información del votante y las encuestas en ejecución que aun no responde.
-  `POST {{host}}/voter/{{cid}}/poll{{slug}}/assign` : Un usuario del tipo chief, manda a llamar en la url el slug de una encuesta para ser llenada por un votante. Igualemnte envía una fecha de expiración vigente en la duración de una encuesta en JSON. Obtiene un token de un solo uso que debe ser compartido con el votante para cargarlo en una unidad autenticada como usuario "nodo" para responder la encuesta.
-  `GET {{host}}/consult/{{token}}/` : En una máquina autenticada con usuario del tipo nodo carga el token de votante previamente recibido. Este devolverá la información del votante, así como el contenido de la encuesta
-  `POST {{host}}/consult/{{token}}/answer/` : En una máquina autenticada con usuario del tipo nodo carga el token de votante previamente recibido, así como las respuestas de la encuesta en JSON. Solo recibirá un mensaje de confirmación del llenado de la encuesta.
-  `GET {{host}}/stats/` : Un usuario del tipo staff enlista las encuestas finalizadas.
-  `POST {{host}}/stats/{{slug}}/` : Un usuario del tipo staff consulta las respuestas del slug de la encuesta enviada. Esta contendrá las preguntas que contiene y la cantidad de respuestas "Si" y "No" que recibió.


## Manejo de backups ##

Los siguientes comandos permiten administrar respaldos de la base de datos. Es importate tener precaución de no borrar el volumen "%postgres_data_backups" para no perder los respaldos.

- Crear backup

> $ docker-compose -f <entorno>.yml exec dbcc backup

- Consultar backups

> $ docker-compose -f <entorno>.yml exec dbcc backups

- Restaurar backups

> $ docker-compose -f <entorno>.yml exec dbcc restore <BACKUP_DESEADO.sql.gz>
