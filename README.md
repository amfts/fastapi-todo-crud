# FastAPI TODO CRUD
API REST para gestionar tareas construida con FastAPI, SQLAlchemy y Docker.


## Descripción
Este proyecto implementa una API REST completa para la gestión de tareas (TODO list) utilizando FastAPI como framework web, SQLAlchemy como ORM para la base de datos y Docker para la containerización.



Incluye tests automatizados con Pytest y documentación automática mediante Swagger UI.




## Tecnologías utilizadas

- FastAPI 0.104.1  

- SQLAlchemy 2.0.23  

- Pydantic 2.5.0  

- Pytest 7.4.3  

- Docker y Docker Compose  

- SQLite (base de datos)


## Características principales

- CRUD completo (Create, Read, Update, Delete)  

- Validación de datos con Pydantic  

- Documentación automática con OpenAPI/Swagger  

- Tests automatizados  

- Containerización con Docker  

- Base de datos relacional con SQLAlchemy ORM


## Instalación



### Requisitos previos



- Python 3.11 o superior  

- Docker y Docker Compose (opcional)



## Opción 1: Ejecución con Docker



```bash

git clone https://github.com/amtfs/fastapi-todo-crud.git

cd fastapi-todo-crud



docker-compose up --build

```



## Opción 2: Ejecución local

```bash

# Clonar el repositorio

git clone https://github.com/amtfs/fastapi-todo-crud.git

cd fastapi-todo-crud


# Crear entorno virtual

python -m venv venv


# Activar entorno virtual

  # En Windows
  
  venv\\Scripts\\activate
  
  # En Linux/Mac
  
  source venv/bin/activate


# Instalar dependencias

pip install -r requirements.txt


# Ejecutar el servidor

uvicorn app.main:app --reload

```



La API estará disponible en:
http://localhost:8000



## Documentación
Una vez el servidor esté en ejecución, puedes acceder a:

- Swagger UI → http://localhost:8000/docs  
- ReDoc → http://localhost:8000/redoc


## Endpoints disponibles

| Método | HTTP Endpoint | Descripción | 
|--------|---------------|-------------| 
| GET | / | Mensaje de bienvenida | 
| POST | /todos/ | Crear una nueva tarea | 
| GET | /todos/ | Obtener lista de todas las tareas | 
| GET | /todos/{id} | Obtener una tarea específica por ID | 
| PUT | /todos/{id} | Actualizar una tarea existente | 
| DELETE | /todos/{id} | Eliminar una tarea |



## Estructura del proyecto
```text

fastapi-todo-crud/

│

├── app/

│   ├── \_\_init\_\_.py

│   ├── main.py          # Punto de entrada de la aplicación

│   ├── models.py        # Modelos de base de datos

│   ├── schemas.py       # Esquemas de validación Pydantic

│   └── database.py      # Configuración de base de datos

│

├── tests/

│   ├── \_\_init\_\_.py

│   └── test\_api.py      # Tests automatizados

│

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── .gitignore

└── README.md

```

## Tests

Para ejecutar los tests:



```bash

pytest tests/ -v

```

Los tests cubren todas las operaciones CRUD y verifican el correcto funcionamiento de los endpoints.



## Ejemplos de uso
### Crear una tarea

```bash

curl -X POST "http://localhost:8000/todos/" -H "Content-Type: application/json" -d '{"title":"Completar proyecto","description":"Finalizar la API REST","completed":false}'

```


### Obtener todas las tareas

```bash

curl http://localhost:8000/todos/

```

### Actualizar una tarea

```bash

curl -X PUT "http://localhost:8000/todos/1" ; -H "Content-Type: application/json" -d '{"completed":true}'

```

### Eliminar una tarea

```bash

curl -X DELETE "http://localhost:8000/todos/1"

```


## Desarrollo

Este proyecto fue desarrollado como parte de mi portfolio de DevOps/Backend, aplicando buenas prácticas como:

- Separación de responsabilidades (modelos, esquemas, lógica de negocio)  

- Testing automatizado  

- Containerización para facilitar el despliegue  

- Documentación automática  

- Validación de datos  

- Manejo de errores HTTP

---



## Autor

Alberto - Ingeniero de Telecomunicaciones




## Licencia

Este proyecto está bajo la Licencia MIT.



