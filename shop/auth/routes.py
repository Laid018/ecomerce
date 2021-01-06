from flask import render_template, redirect, url_for, request, session, flash
from shop import db
from . import auth_bp
from .forms import RegistrationForm, LoginForm
from .models import User


@auth_bp.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        pw = User.set_password(form.password.data)
        name = form.name.data
        username = form.username.data
        email = form.email.data

        user = User.get_by_email(email)
        if user is not None:
            flash(f'El {email} ya esta siendo utilizado.', 'danger')
        else:
            user = User(name=name, username=username, email=email, password=pw)
            db.session.add(user)
            db.session.commit()
            flash(f'Bienvenid@ {name} gracias por registrarte.', 'success')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth_bp.route('/login/', methods=['GET','POST'])
def login():
    if 'email' in session:
        return redirect(url_for('public.home'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data

        user = User.get_by_email(email)
        if user is not None and user.check_password(password):
            session['email'] = email
            flash(f'Bienvenido {user.name}', 'success')
            return redirect(request.args.get('next') or url_for('public.home'))
        else:
            flash(f'Error. Email y/o clave incorrectos. \nIntenta nuevamente', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
