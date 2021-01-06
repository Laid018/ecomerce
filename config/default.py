from os.path import dirname, abspath
import os

# Directorio de la app
BASE_DIR = dirname(dirname(abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, '/shop/static/imagenes/')
print(IMAGES_DIR)
# SecretKey
SECRET_KEY = "lsjfsafnbmzcbasdayt734674621894ygvczfrancgdsaf78491kadudf78fs910"

# Config SQLALchemy
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:'+''+'@localhost:3306/myshop'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Variables de entorno
APP_ENV = ""
APP_ENV_DEVELOPMENT = "development"
APP_ENV_LOCAL = "local"
APP_ENV_PRODUCTION = "production"
APP_ENV_TESTING = "testing"

