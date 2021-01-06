from flask import render_template, session, redirect, url_for, request,flash
from shop.products.models import Product
from . import public_bp

# Página de inicio
@public_bp.route('/')
def principal():
    if 'email' in session:
        return redirect(url_for('public.home'))
    products = Product.query.all()
    return render_template('home/index.html', products=products)

# Página ya logueado
@public_bp.route('/home/')
def home():
    if 'email' in session:
        products = Product.query.all()
        return render_template('home/principal.html', products=products)
    else:
        return redirect(url_for('auth.login'))

# Página de contacto
@public_bp.route('/contact/')
def contact():
    return render_template('home/contact.html')
