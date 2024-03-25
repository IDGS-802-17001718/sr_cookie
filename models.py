from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

db = SQLAlchemy()

class Roles(db.Model):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rol = Column(String(100))
    descripcion = Column(String(255))
    acceso = Column(Boolean, default=True)
    aniadir = Column(Boolean, default=True)
    eliminar = Column(Boolean, default=True)
    modificar = Column(Boolean, default=True)

class Users(db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String(100))
    correo = Column(String(255))
    contrasenia = Column(String(255))
    rol_id = Column(Integer, ForeignKey('roles.id'))
    status = Column(Integer, default=1)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.now)
    creado_por = Column(Integer, ForeignKey('usuarios.id'))
    fecha_modificacion = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modificado_por = Column(Integer, ForeignKey('usuarios.id'))

class Suppliers(db.Model):
    __tablename__ = 'proveedores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    rfc = Column(String(100))
    correo = Column(String(255))
    telefono = Column(String(20))
    status = Column(Integer, default=1)

