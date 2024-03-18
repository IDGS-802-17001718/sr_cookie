""" If you need to add more imports, add them in another line."""
from wtforms import Form, StringField, EmailField, SelectField, RadioField, IntegerField, DateField, validators, TextAreaField

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

class SupplierForm(Form):
    id = IntegerField("id")
    name=StringField("name",[validators.DataRequired(message='El campo es requerido'), validators.length(min=4, max=20, message="Ingrese un nombre valido")])
    email=EmailField("email",[validators.DataRequired(message='El campo es requerido'), validators.length(min=6, max=100, message="Ingrese un correo valido"), validators.Email(message="Ingrese un correo valido")])
    phone=StringField("phone",[validators.DataRequired(message='El campo es requerido'), validators.length(min=6, max=20, message="Ingrese un telefono valido"), validators.Regexp('^[0-9]*$', message="Ingrese un telefono valido")])
    address= TextAreaField("address",[validators.DataRequired(message='El campo es requerido')], render_kw={"rows": 5, "cols": 40})
    state=StringField("state",[validators.DataRequired(message='El campo es requerido')])
    zip=StringField("zip",[validators.DataRequired(message='El campo es requerido')])




    