from flask_wtf import FlaskForm as Formulir
from wtforms import (
    StringField, TextAreaField, 
    SelectField, SubmitField
)
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms.widgets import html_params, HTMLString

class AnggotaForm(Formulir):
    no_anggota = StringField('Nomor Anggota', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    namaanggota = StringField('Nama Anggota', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    kirim = SubmitField('Tambah')
