from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired,  Email, EqualTo
from app.models import User

class MasukForm(FlaskForm):
    namauser = StringField('Nama User', validators=[DataRequired(message='Wajib diisi')])
    katasandi = PasswordField('Kata Sandi', validators=[DataRequired(message='Wajib diisi')])
    ingat_saya =  BooleanField('Ingat Saya')
    kirim = SubmitField('Sign In')

class DaftarForm(FlaskForm):
    namauser = StringField('Nama User', validators=[DataRequired(message='Wajib diisi')])
    surel = StringField('Email', validators=[DataRequired(message='Wajib diisi'), Email(message='Format email salah')])
    katasandi = PasswordField('Kata Sandi', validators=[DataRequired(message='Wajib diisi')])
    c_katasandi = PasswordField(
        'Ulangi Kata Sandi', validators=[DataRequired(message='Wajib diisi'), EqualTo('katasandi', 'Password tidak cocok')])
    kirim = SubmitField('Daftar')

    def validate_namauser(self, namauser):
        u = User.query.filter_by(username=namauser.data).first()
        if u is not None:
            raise ValidationError('Username sudah dipakai')
    
    def validate_surel(self, surel):
        u = User.query.filter_by(email=surel.data).first()
        if u is not None:
            raise ValidationError('Email sudah digunakan')