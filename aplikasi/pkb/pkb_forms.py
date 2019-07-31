from flask_wtf import FlaskForm as Formulir
from wtforms import (
    StringField, IntegerField, 
    SubmitField
)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, NumberRange, Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from aplikasi.inseminasi.inseminasi_models import Inseminasi

def inseminasi():
    return Inseminasi.query.all()

class PkbForm(Formulir):
    inseminasi = QuerySelectField('Inseminasi',      
                               validators=[Required()],
                               query_factory=inseminasi)
    sem_code = StringField('Kode Semen', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    batch = StringField('Batch', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])  
    ib_hasil = IntegerField('IB-Ke', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=0, max=1)])
    tgl_pkb = DateField('Tanggal PKB', format='%Y-%m-%d')
    kirim = SubmitField('Tambah')

