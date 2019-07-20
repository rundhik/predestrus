from flask_wtf import FlaskForm as Formulir
from wtforms import (
    StringField, IntegerField, 
    DateField, SubmitField
)
from wtforms.validators import DataRequired, Length, NumberRange
class SapiForm(Formulir):
    no_sapi = StringField('Nomor Telinga', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    fitur1 = IntegerField('Fitur 1', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=10)])
    fitur2 = IntegerField('Fitur 2', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=10)])
    fitur3 = IntegerField('Fitur 3', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=10)])
    laktasi = IntegerField('Laktasi', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=4)])
    ib = DateField('IB ke-', id='ib')
    pkb = DateField('PKB', id='pkb')
    kirim = SubmitField('Tambah')