""" If you need to add more imports, add them in another line."""
from wtforms import Form, StringField, EmailField, SelectField, RadioField, IntegerField, DateField, validators

"""If you need to add more fields to the form or change the validation rules, modify the classes below"""

class loginForm(Form):
    username = StringField("Username", [validators.length(min=4, max=20, message="Ingrese un nombre de usuario valido")])
    email = EmailField("Email", [validators.length(min=6, max=100, message="Ingrese un correo valido")])
    password = StringField("Password", [validators.length(min=4, max=20, message="Ingrese una contraseña valida")])
class UserForm(Form):
    username = StringField("Username", [validators.length(min=4, max=20, message="Ingrese un nombre de usuario valido")])
    userlastname = StringField("Userlastname", [validators.length(min=4, max=20, message="Ingrese un apellido valido")])
    email = EmailField("Email", [validators.length(min=6, max=100, message="Ingrese un correo valido")])
    password = StringField("Password", [validators.length(min=4, max=20, message="Ingrese una contraseña valida")])
    role = SelectField("Role", choices=[("admin", "Admin"), ("user", "User")])
class supplierForm(Form):
    name=StringField("name",[validators.DataRequired(message='El campo es requerido')])
    email=EmailField("email",[validators.Email(message="Ingrese un correo valido")])
    phone=IntegerField("phone",[validators.number_range(min=1, max=20, message='Valor no valido')])
    address=StringField("address",[validators.DataRequired(message='El campo es requerido')])
    city=StringField("city",[validators.DataRequired(message='El campo es requerido')])
    state=StringField("state",[validators.DataRequired(message='El campo es requerido')])
    zip=IntegerField("zip",[validators.number_range(min=1, max=20, message='Valor no valido')])



    