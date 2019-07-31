from flask_wtf import FlaskForm as Formulir
from wtforms import (
    StringField, PasswordField,
    SubmitField, BooleanField
)
from wtforms.validators import (
    DataRequired, Length, ValidationError,
    NumberRange, EqualTo
    )
from aplikasi.user.user_models import User

class MasukForm(Formulir):
    namauser = StringField('Nama User', validators=[DataRequired(message='Wajib diisi')])
    katasandi = PasswordField('Kata Sandi', validators=[DataRequired(message='Wajib diisi')])
    ingat_saya =  BooleanField('Ingat Saya')
    kirim = SubmitField('Masuk')

class DaftarForm(Formulir):
    namauser = StringField('Nama User', validators=[DataRequired(message='Wajib diisi')])
    katasandi = PasswordField('Kata Sandi', validators=[DataRequired(message='Wajib diisi')])
    c_katasandi = PasswordField(
        'Ulangi Kata Sandi', validators=[DataRequired(message='Wajib diisi'), EqualTo('katasandi', 'Password tidak cocok')])
    kirim = SubmitField('Daftar')

    def validate_namauser(self, namauser):
        u = User.query.filter_by(username=namauser.data).first()
        if u is not None:
            raise ValidationError('Username sudah dipakai')