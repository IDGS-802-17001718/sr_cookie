
""" Flask imports Start"""
from flask import Flask, request, render_template, Response, redirect, url_for, flash, g
from flask_wtf.csrf import CSRFProtect
import forms
from config import DevelopmentConfig
from models import db
from datetime import datetime, timedelta
from sqlalchemy import func

""" Flask imports End"""


""" Tip 1: Comment the code, it will help you to understand the code later. """

""" Allways start the comment using three double quotes and write 'Start'. """
""" Allways close the comment using three double quotes and write 'End'. """


app=Flask(__name__) 
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()
    
"""  Error handler Start 
     Error handler, when the user try to access a page that doesn't exist this will bee shown"""
@app.errorhandler(400)
def page_not_found(e):
    return render_template('404.html'),404
""" Error handler end """

""" Index Start """
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=='POST':
        return render_template("index.html")
    return render_template("index.html")
""" Index End """

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()