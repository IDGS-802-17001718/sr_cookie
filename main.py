
""" Flask imports Start"""
from flask import Flask, request, render_template, Response, redirect, url_for, flash, jsonify, g
from flask_wtf.csrf import CSRFProtect
import forms
from config import DevelopmentConfig
from models import db
from datetime import datetime, timedelta
from sqlalchemy import func
import models

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

@app.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    form = forms.SupplierForm()
    if request.method == 'POST':
        form = forms.SupplierForm()
        if form.validate_on_submit():
            if db.session.query(models.Suppliers).filter(models.Suppliers.email == form.email.data).first():
                flash('Email already exists', 'danger')
                return redirect(url_for('suppliers'))
            if db.session.query(models.Suppliers).filter(models.Suppliers.phone == form.phone.data).first():
                flash('Phone already exists', 'danger')
                return redirect(url_for('suppliers'))
            if db.session.query(models.Suppliers).filter(models.Suppliers.name == form.name.data).first():
                flash('Name already exists', 'danger')
                return redirect(url_for('suppliers'))
            if form.phone.data.isdigit() == False:
                flash('Phone must be a number', 'danger')
                return redirect(url_for('suppliers'))
            
            supplier = suppliers(
                name=form.name.data,
                email=form.email.data,
                phone=form.phone.data,
                address=form.address.data,
                city=form.city.data,
                state=form.state.data,
                zip=form.zip.data,
                country=form.country.data
            )
            db.session.add(supplier)
            db.session.commit()
            flash('Supplier added successfully', 'success')
            return redirect(url_for('suppliers'))
        else:
            flash('Error adding supplier', 'danger')
            return redirect(url_for('suppliers'))
    if request.method == 'GET':
        return render_template('suppliers.html', form= form, suppliers=db.session.query(models.Suppliers).all())

@app.route('/suppliers/edit/<int:id>', methods=['GET', 'POST'])
def edit_supplier(id):
    supplier = db.session.query(models.Suppliers).get(id)
    form = forms.SupplierForm(obj=supplier)
    if request.method == 'POST':
        form = forms.SupplierForm()
        if form.validate_on_submit():
            if db.session.query(models.Suppliers).filter(models.Suppliers.email == form.email.data).first():
                flash('Email already exists', 'danger')
                return redirect(url_for('suppliers'))
            if db.session.query(models.Suppliers).filter(models.Suppliers.phone == form.phone.data).first():
                flash('Phone already exists', 'danger')
                return redirect(url_for('suppliers'))
            if db.session.query(models.Suppliers).filter(models.Suppliers.name == form.name.data).first():
                flash('Name already exists', 'danger')
                return redirect(url_for('suppliers'))
            if form.phone.data.isdigit() == False:
                flash('Phone must be a number', 'danger')
                return redirect(url_for('suppliers'))
            supplier.name = form.name.data
            supplier.email = form.email.data
            supplier.phone = form.phone.data
            supplier.address = form.address.data
            supplier.city = form.city.data
            supplier.state = form.state.data
            supplier.zip = form.zip.data
            supplier.country = form.country.data
            db.session.commit()
            flash('Supplier updated successfully', 'success')
            return redirect(url_for('suppliers'))
        else:
            flash('Error updating supplier', 'danger')
            return redirect(url_for('suppliers'))
    if request.method == 'GET':
        return render_template('edit_supplier.html', form= form, supplier=supplier)
    
@app.route('/suppliers/delete/<int:id>', methods=['DEKETE'])
def delete_supplier(id):
    supplier = db.session.query(models.Suppliers).get(id)
    db.session.delete(supplier)
    db.session.commit()
    flash('Supplier deleted successfully', 'success')
    return redirect(url_for('suppliers'))

@app.route('/suppliers/save', methods=['POST'])
def save_supplier():
    form = forms.SupplierForm()
    if form.validate():
        if db.session.query(models.Suppliers).filter(models.Suppliers.email == form.email.data).first():
            flash('Email already exists', 'danger')
            return redirect(url_for('suppliers'))
        if db.session.query(models.Suppliers).filter(models.Suppliers.phone == form.phone.data).first():
            flash('Phone already exists', 'danger')
            return redirect(url_for('suppliers'))
        if db.session.query(models.Suppliers).filter(models.Suppliers.name == form.name.data).first():
            flash('Name already exists', 'danger')
            return redirect(url_for('suppliers'))
        if form.phone.data.isdigit() == False:
            flash('Phone must be a number', 'danger')
            return redirect(url_for('suppliers'))
        if form.id != -1:
            supplier = db.session.query(models.Suppliers).get(form.id)
            supplier.name = form.name.data
            supplier.email = form.email.data
            supplier.phone = form.phone.data
            supplier.address = form.address.data
            supplier.city = form.city.data
            supplier.state = form.state.data
            supplier.zip = form.zip.data
            supplier.country = form.country.data
            db.session.commit()
            flash('Supplier updated successfully', 'success')
            return redirect(url_for('suppliers'))
        else:
            supplier = suppliers(
                name=form.name.data,
                email=form.email.data,
                phone=form.phone.data,
                address=form.address.data,
                city=form.city.data,
                state=form.state.data,
                zip=form.zip.data,
                country=form.country.data
            )
            db.session.add(supplier)
            db.session.commit()
            flash('Supplier added successfully', 'success')
            return redirect(url_for('suppliers'))
    else:
        flash('Error adding supplier', 'danger')
        return redirect(url_for('suppliers'))


@app.route('/suppliers/getall', methods=['GET'])
def get_all_suppliers():
    print("entrando a get_all_suppliers")
    suppliers = db.session.query(models.Suppliers).all()
    serialized_suppliers = []
    for supplier in suppliers:
        serialized_supplier = {
            'id': supplier.id,
            'name': supplier.name,
            'email': supplier.email,
            'phone': supplier.phone,
            'address': supplier.address,
            'city': supplier.city,
            'state': supplier.state,
            'zip': supplier.zip,
            'country': supplier.country,
            'status': supplier.status
        }
        serialized_suppliers.append(serialized_supplier)
    print(serialized_suppliers)
    response = {
        "data": serialized_suppliers
    }
    return jsonify(response)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()