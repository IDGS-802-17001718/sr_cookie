# app/__init__.py

from flask import Flask
from config import DevelopmentConfig
from .suppliers.views import suppliers_bp

def create_app():
    app=Flask(__name__) 
    app.config.from_object(DevelopmentConfig)
    
    # Configuración de la aplicación

    # Registrar blueprints
    app.register_blueprint(suppliers_bp, url_prefix='/suppliers')

    return app
