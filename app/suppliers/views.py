# app/auth/views.py

from flask import Blueprint, render_template, request
from flask import redirect, url_for, flash
from forms import SupplierForm
from models import db, Suppliers

suppliers_bp = Blueprint('suppliers', __name__)


@suppliers_bp.route('/')
def index():
    form = SupplierForm()
    suppliers = Suppliers.query.all()
    return render_template("suppliers.html", suppliers = suppliers, form = form)

@suppliers_bp.route('/save', methods=['POST'])
def save():
    form = SupplierForm(request.form)
    print("entro al post")
    try:
        print("entro al try")
        if form.validate():
            if form.id.data != 0:
                print(form.id.data)
                supplier = Suppliers.query.filter_by(id = form.id.data).first()
                print(supplier)
                if supplier == None:
                    flash('Supplier not found', 'danger')
                    return redirect(url_for('suppliers.index'))
                supplier.nombre = form.nombre.data
                supplier.rfc = form.rfc.data
                supplier.correo = form.correo.data
                supplier.telefono = form.telefono.data
                db.session.commit()
                flash('Supplier updated successfully', 'success')
                return redirect(url_for('suppliers.index'))
            else:
                supplier = Suppliers(nombre = form.nombre.data, 
                            rfc = form.rfc.data, 
                            correo = form.correo.data,
                            telefono = form.telefono.data)
                print("supplier creado")
                db.session.add(supplier)
                print("supplier agregado")
                db.session.commit()
                print("supplier guardado")
                flash('Supplier added successfully', 'success')
                return redirect(url_for('suppliers.index'))
        else:
            print(form.errors)
            flash('Form validation failed', 'danger')
            return redirect(url_for('suppliers.index'))
    except Exception as e:
        print(e)
        flash('Error adding supplier: {}'.format(e), 'danger')
        return redirect(url_for('suppliers.index'))

@suppliers_bp.route('/delete', methods=['POST'])
def delete():
    id = request.form.get('id')
    supplier = Suppliers.query.filter_by(id = id).first()
    supplier.status = 0
    db.session.commit()
    flash('Supplier deactivated successfully', 'success')
    return redirect(url_for('suppliers.index'))



