from flask import render_template,redirect,url_for,request,session,flash,current_app
from werkzeug.utils import secure_filename
from . import products_bp
from shop import db 
from .models import Brand,Category,Product
from .forms import AddProduct
import os

@products_bp.route('/addbrand/', methods=['GET','POST'])
def addbrand():
    if 'email' in session:
        if request.method == "POST":
            getbrand = request.form.get('brand')
            brand = Brand(name=getbrand) 
            db.session.add(brand) 
            db.session.commit()
            flash(f'La marca {getbrand} fue agregada sastifactoriamente.', 'success') 
            return redirect(url_for('products.addbrand'))
        return render_template('products/addbrand.html', brands='brands')
    else:
        return redirect(url_for('auth.login'))

@products_bp.route('/addcategory/', methods=['GET','POST'])
def addcategory():
    if 'email' in session:
        if request.method == "POST":
            getcategory = request.form.get('category')
            category = Category(name=getcategory) 
            db.session.add(category) 
            db.session.commit()
            flash(f'La categoria {getcategory} fue agregada sastifactoriamente.', 'success') 
            return redirect(url_for('products.addcategory'))
        return render_template('products/addbrand.html', categories='categories')
    else:
        return redirect(url_for('auth.login'))

@products_bp.route('/addproduct/', methods=['GET','POST'])
def addproduct():
    if 'email' in session:
        brands = Brand.query.all()
        categories = Category.query.all()
        form = AddProduct(request.form)
        if request.method == 'POST':
            name = form.name.data
            price = form.price.data
            disconunt = form.discount.data
            stock = form.stock.data
            colors = form.colors.data
            description = form.description.data
            brand = request.form.get('brand')
            category = request.form.get('category')
            file1 = request.files.get('image_1')
            file2 = request.files.get('image_2')
            file3 = request.files.get('image_3')
            image1_name = None
            image2_name = None
            image3_name = None
            if file1 and file2 and file3:
                image1_name = secure_filename(file1.filename)
                image2_name = secure_filename(file2.filename)
                image3_name = secure_filename(file3.filename)
                image_dir = current_app.config['IMAGES_DIR']
                os.makedirs(image_dir, exist_ok=True)
                file_path1 = os.path.join(image_dir, image1_name)
                file_path2 = os.path.join(image_dir, image2_name)
                file_path3 = os.path.join(image_dir, image3_name)
                file1.save(file_path1)
                file2.save(file_path2)
                file3.save(file_path3)
                addproduct = Product(name=name,price=price,discount=disconunt,stock=stock,colors=colors,description=description,brand_id=brand,category_id=category,image_1=image1_name,image_2=image2_name,image_3=image3_name)
                db.session.add(addproduct)
                db.session.commit()
                flash(f'Se agrego correctamente el producto {name}','success')
                return redirect(url_for('public.home'))
        return render_template('products/addproduct.html', form=form,brands=brands,categories=categories)
    else:
        return redirect(url_for('auth.login'))


@products_bp.route('/showproducts/')
def showproducts():
    if 'email' not in session:
        flash('Accede al sistema primero')
        return redirect(url_for('auth.login'))
    products = Product.query.all()
    return render_template('home/index.html', products=products)

@products_bp.route('/dashboard/', methods=['POST','GET'])
def dashboard():
    if 'email' not in session:
        flash('Debe iniciar sesión')
        return redirect(url_for('auth.login'))
    return render_template('admin/dash.html')

