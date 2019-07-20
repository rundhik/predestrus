from flask_wtf import FlaskForm as Formulir
from wtforms import (
    StringField, TextAreaField, 
    SelectField, SubmitField
)
from wtforms.validators import DataRequired, Length, Email, NumberRange

class WilayahForm(Formulir):
    namawilayah = StringField(
        'Nama Wilayah', 
        validators=[DataRequired(message='Tidak boleh kosong'), 
        Length(max=30)]
        )
    kirim = SubmitField('Tambah')