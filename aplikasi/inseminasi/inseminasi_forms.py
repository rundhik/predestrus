from flask_wtf import FlaskForm as Formulir
from wtforms import (
    StringField, IntegerField, 
    SubmitField
)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, NumberRange, Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from aplikasi.sapi.sapi_models import Sapi

def sapi():
    return Sapi.query.all()

class InseminasiForm(Formulir):
    sapi = QuerySelectField('Sapi',      
                               validators=[Required()],
                               query_factory=sapi)
    sem_code = StringField('Kode Semen', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    batch = StringField('Batch', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    rpf = IntegerField('RPF', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=10)])
    perilaku = IntegerField('Perilaku', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=10)])
    ib_ke = IntegerField('IB-Ke', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=10)])
    jarak_ib = IntegerField('Jarak IB', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=10)])
    laktasi = IntegerField('Laktasi', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=4)])
    tgl_ib = DateField('Tanggal IB', format='%Y-%m-%d')
    kirim = SubmitField('Tambah')

