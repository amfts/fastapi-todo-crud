FastAPI TODO CRUD



API REST para gestionar tareas construida con FastAPI, SQLAlchemy y Docker.

Descripción



Este proyecto implementa una API REST completa para la gestión de tareas (TODO list) utilizando FastAPI como framework web, SQLAlchemy como ORM para la base de datos, y Docker para la containerización. Incluye tests automatizados con Pytest y documentación automática mediante Swagger UI.

Tecnologías utilizadas



&nbsp;   FastAPI 0.104.1

&nbsp;   SQLAlchemy 2.0.23

&nbsp;   Pydantic 2.5.0

&nbsp;   Pytest 7.4.3

&nbsp;   Docker y Docker Compose

&nbsp;   SQLite (base de datos)



Características principales



&nbsp;   CRUD completo (Create, Read, Update, Delete)

&nbsp;   Validación de datos con Pydantic

&nbsp;   Documentación automática con OpenAPI/Swagger

&nbsp;   Tests automatizados

&nbsp;   Containerización con Docker

&nbsp;   Base de datos relacional con SQLAlchemy ORM



Instalación

Requisitos previos



&nbsp;   Python 3.11 o superior

&nbsp;   Docker y Docker Compose (opcional)



Opción 1: Ejecución con Docker



bash

Copy

git clone https://github.com/amtfs/fastapi-todo-crud.git  

cd fastapi-todo-crud  

docker-compose up --build  



Opción 2: Ejecución local



bash

Copy

\# Clonar el repositorio  

git clone https://github.com/amtfs/fastapi-todo-crud.git  

cd fastapi-todo-crud  

&nbsp; 

\# Crear entorno virtual  

python -m venv venv  

&nbsp; 

\# Activar entorno virtual  

\# En Windows:  

venv\\Scripts\\activate  

\# En Linux/Mac:  

source venv/bin/activate  

&nbsp; 

\# Instalar dependencias  

pip install -r requirements.txt  

&nbsp; 

\# Ejecutar el servidor  

uvicorn app.main:app --reload  



La API estará disponible en http://localhost:8000

Documentación



Una vez el servidor esté en ejecución, puedes acceder a:



&nbsp;   Documentación interactiva (Swagger UI): http://localhost:8000/docs

&nbsp;   Documentación alternativa (ReDoc): http://localhost:8000/redoc



Endpoints disponibles

Método HTTP	Endpoint	Descripción

GET	/	Mensaje de bienvenida

POST	/todos/	Crear una nueva tarea

GET	/todos/	Obtener lista de todas las tareas

GET	/todos/{id}	Obtener una tarea específica por ID

PUT	/todos/{id}	Actualizar una tarea existente

DELETE	/todos/{id}	Eliminar una tarea

Estructura del proyecto



fastapi-todo-crud/  

├── app/  

│   ├── \_\_init\_\_.py  

│   ├── main.py          # Punto de entrada de la aplicación  

│   ├── models.py        # Modelos de base de datos  

│   ├── schemas.py       # Esquemas de validación Pydantic  

│   └── database.py      # Configuración de base de datos  

├── tests/  

│   ├── \_\_init\_\_.py  

│   └── test\_api.py      # Tests automatizados  

├── Dockerfile  

├── docker-compose.yml  

├── requirements.txt  

├── .gitignore  

└── README.md  



Tests



Para ejecutar los tests:



bash

Copy

pytest tests/ -v  



Los tests cubren todas las operaciones CRUD y verifican el correcto funcionamiento de los endpoints.

Ejemplos de uso

Crear una tarea



bash

Copy

curl -X POST "http://localhost:8000/todos/" \\  

&nbsp; -H "Content-Type: application/json" \\  

&nbsp; -d '{"title":"Completar proyecto","description":"Finalizar la API REST","completed":false}'  



Obtener todas las tareas



bash

Copy

curl http://localhost:8000/todos/  



Actualizar una tarea



bash

Copy

curl -X PUT "http://localhost:8000/todos/1" \\  

&nbsp; -H "Content-Type: application/json" \\  

&nbsp; -d '{"completed":true}'  



Eliminar una tarea



bash

Copy

curl -X DELETE "http://localhost:8000/todos/1"  



Desarrollo



Este proyecto fue desarrollado como parte de mi portfolio de DevOps/Backend, aplicando buenas prácticas de desarrollo como:



&nbsp;   Separación de responsabilidades (modelos, esquemas, lógica de negocio)

&nbsp;   Testing automatizado

&nbsp;   Containerización para facilitar el despliegue

&nbsp;   Documentación automática

&nbsp;   Validación de datos

&nbsp;   Manejo de errores HTTP



Autor



Alberto - Ingeniero de Telecomunicaciones



Licencia



Este proyecto está bajo la Licencia MIT.

