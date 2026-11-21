# AsteroidGuard API

Microservicio RESTful diseñado para evaluar el riesgo de impacto de asteroides cercanos a la Tierra (NEOs), persistir el historial de predicciones en PostgreSQL y desplegarse de forma reproducible mediante Docker Compose.

## Arquitectura y Stack Tecnológico

* **Backend & API:** Python 3.11, FastAPI, Pydantic v2, Uvicorn
* **Motor de Inferencia:** NumPy (clasificación probabilística mediante combinación lineal normalizada y activación sigmoide)
* **Base de Datos y ORM:** PostgreSQL 16, SQLAlchemy 2.0
* **Infraestructura:** Docker, Docker Compose (con *healthchecks* y volúmenes persistentes)

## Estructura del Proyecto

```text
asteroid-guard-api/
├── app/
│   ├── main.py          # Endpoints REST y ciclo de vida de la API
│   ├── schemas.py       # Esquemas de validación de entrada/salida (Pydantic)
│   ├── predictor.py     # Lógica de normalización e inferencia con NumPy
│   ├── models.py        # Modelos relacionales (SQLAlchemy ORM)
│   └── database.py      # Configuración de sesión y conexión a PostgreSQL
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
