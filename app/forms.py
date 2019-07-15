from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    namauser = StringField('Nama User', validators=[DataRequired()])
    katasandi = PasswordField('Kata Sandi', validators=[DataRequired()])
    ingat_saya =  BooleanField('Ingat Saya')
    kirim = SubmitField('Sign In')