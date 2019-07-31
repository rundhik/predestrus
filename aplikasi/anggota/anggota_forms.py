from flask_wtf import FlaskForm as Formulir
from wtforms import (
    StringField, TextAreaField, 
    SelectField, SubmitField
)
from wtforms.validators import DataRequired, Length, Email, NumberRange, Required
from wtforms.widgets import html_params, HTMLString
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from aplikasi.wilayah.wilayah_models import Wilayah

def wilayah():
    return Wilayah.query.all()

class AnggotaForm(Formulir):
    no_anggota = StringField('Nomor Anggota', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    namaanggota = StringField('Nama Anggota', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    wilayah = QuerySelectField('Wilayah',      
                               validators=[Required()],
                               query_factory=wilayah)
    kirim = SubmitField('Tambah')
