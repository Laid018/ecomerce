from wtforms import Form,StringField,IntegerField,BooleanField,SubmitField, TextAreaField, validators
from flask_wtf.file import FileAllowed, FileField,FileRequired

class AddProduct(Form):
    name = StringField('Nombre',[validators.DataRequired()])
    price = IntegerField('Precio',[validators.DataRequired()])
    discount = IntegerField('Descuento',default=0)
    stock = IntegerField('Stock',[validators.DataRequired()])
    description = TextAreaField('Descripción',[validators.DataRequired()])
    colors = TextAreaField('Colores',[validators.DataRequired()])

    image_1 = FileField('Imagen 1',validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'], 'Imágenes solamente, por favor.')])

    image_2 = FileField('Imagen 2',validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'], 'Imágenes solamente, por favor.')])
    image_3 = FileField('Imagen 3',validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'], 'Imágenes solamente, por favor.')])
