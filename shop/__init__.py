from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .auth.models import User
from .products.models import Brand,Category

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    # Inicializar elementos
    db = SQLAlchemy(app)
    db.create_all()

    # Registrar blueprints de la app
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    from .public import public_bp
    app.register_blueprint(public_bp)
    from .admin import admin_bp
    app.register_blueprint(admin_bp)
    from .products import products_bp
    app.register_blueprint(products_bp)

    return app
