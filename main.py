
""" Flask imports Start"""
from flask import Flask, request, render_template, Response 
from flask import redirect, url_for, flash, jsonify, g, Blueprint, abort
from flask_wtf.csrf import CSRFProtect
from jinja2 import TemplateNotFound
import forms
from config import DevelopmentConfig
from models import db
from datetime import datetime, timedelta
from sqlalchemy import func
import models
from app import create_app

""" Flask imports End"""
app= create_app()

""" Tip 1: Comment the code, it will help you to understand the code later. """

""" Allways start the comment using three double quotes and write 'Start'. """
""" Allways close the comment using three double quotes and write 'End'. """


csrf = CSRFProtect()
"""  The code below is a route that will be used to show the home page of the application"""

"""  Error handler Start 
     Error handler, when the user try to access a page that doesn't exist this will bee shown"""
@app.errorhandler(400)
def page_not_found(e):
    print(e)
    return render_template('404.html'),404
""" Error handler end """
if __name__ == "__main__":
    
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)