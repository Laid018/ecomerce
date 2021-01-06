from wtforms import Form,BooleanField,StringField,PasswordField,validators

class RegistrationForm(Form):
    name = StringField('Nombre',[validators.DataRequired(), validators.Length(min=4, max=30)])
    username = StringField('Usuario',[validators.DataRequired(), validators.Length(min=4, max=30)])
    email = StringField('Email', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Clave', [validators.DataRequired(), validators.EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Repetir Clave')


class LoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Clave', [validators.DataRequired()])
