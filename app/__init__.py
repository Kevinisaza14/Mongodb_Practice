import os
from flask import Flask, g
from pymongo import MongoClient
from typing import Optional
from flask import current_app
from flask import current_app

# app/__init__.py
# Inicialización de la aplicación Flask y conexión a MongoDB.
# Uso: from app import create_app; app = create_app()


def create_app(config: Optional[dict] = None) -> Flask:
    """
    Factory para crear la aplicación Flask y exponer la conexión a MongoDB.
    Configuraciones por defecto pueden overridearse con variables de entorno
    o pasando un dict `config`.
    Variables de entorno usadas:
      - MONGO_URI (por defecto: mongodb://localhost:27017)
      - MONGO_DBNAME (por defecto: mongodb_practice)
      - SECRET_KEY (por defecto: dev)
    """
    app = Flask(__name__, instance_relative_config=False)

    # configuración por defecto
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev"),
        MONGO_URI=os.getenv("MONGO_URI", "mongodb://localhost:27017"),
        MONGO_DBNAME=os.getenv("MONGO_DBNAME", "mongodb_practice"),
    )

    # sobrescribir con config pasado explícitamente
    if config:
        app.config.update(config)

    # inicializar cliente MongoDB (reutilizable y thread-safe)
    client = MongoClient(app.config["MONGO_URI"])
    db = client[app.config["MONGO_DBNAME"]]

    # guardar en extensiones de la app para acceso centralizado
    app.extensions = getattr(app, "extensions", {})
    app.extensions["mongo_client"] = client
    app.extensions["mongo_db"] = db

    # antes de cada request, poner la db en `g` para acceso fácil
    @app.before_request
    def attach_db():
        g.db = app.extensions["mongo_db"]

    # opcional: teardown (no es estrictamente necesario cerrar MongoClient
    # porque es thread-safe, pero dejamos el hook para limpieza si se requiere)
    @app.teardown_appcontext
    def teardown_db(exc):
        # si se quisiera cerrar el cliente en shutdown, descomentar:
        # client.close()
        return None

    # registrar blueprints si existen (evita error si no están aún creados)
    try:
        from . import routes  # pragma: no cover
        if hasattr(routes, "bp"):
            app.register_blueprint(routes.bp)
    except Exception:
        # no registrar si no existe el módulo aún
        pass

    return app


# Helpers públicos para acceder a la DB desde otros módulos
def get_db():
    """
    Devuelve la instancia de la base de datos activa.
    Uso dentro de vistas o servicios: db = get_db()
    """
    return current_app.extensions["mongo_db"]


def get_client():
    """Devuelve el MongoClient asociado a la app."""
    return current_app.extensions["mongo_client"]