from datetime import datetime

from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm as Formulir
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from wtforms import (
    StringField, TextAreaField, SelectField, 
    RadioField, DateField, IntegerField, SubmitField, widgets
)
from flask_datepicker import datepicker
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms.widgets import html_params, HTMLString
from sqlalchemy import func
from konfigurasi import DevConfig


apl = Flask(__name__)
apl.config.from_object(DevConfig)
db = SQLAlchemy(apl)
migrate = Migrate(apl, db)
bootstrap = Bootstrap(apl)
moment = Moment(apl)
@apl.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    apl.run()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False, index=True, unique=True)
    password = db.Column(db.String(255))
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamps(), onupdate=db.func.current_timestamp())

    def __init__(self, username):
        self.username = username
    
    def __repr__(self):
        return '<user : {}>'.format(self.username)

class Wilayah(db.Model):
    __tablename__ = 'wilayah'
    id = db.Column(db.Integer(), primary_key=True)
    namawilayah = db.Column(db.String(255), nullable=False, index=True)
    anggotas = db.relationship(
        'Anggota',
        backref='anggota',
        lazy='dynamic'
    )
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamps(), onupdate=db.func.current_timestamp())

    def __init__(self, namawilayah):
        self.namawilayah = namawilayah
    
    def __repr__(self):
        return '<wilayah : {}>'.format(self.namawilayah)

class Anggota(db.Model):
    __tablename__ = 'anggota'
    id = db.Column(db.Integer(), primary_key=True)
    no_anggota = db.Column(db.String(255))
    namaanggota = db.Column(db.String(255), nullable=False, index=True)
    wilayah = db.Column(db.Integer(), db.ForeignKey('wilayah.id'))
    sapis = db.relationship(
        'Sapi',
        backref='sapi',
        lazy='dynamic'
    )
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamps(), onupdate=db.func.current_timestamp())

    def __init__(self, namaanggota):
        self.namaanggota = namaanggota
    
    def __repr__(self):
        return '<nama anggota : {}>'.format(self.namaanggota)

class Sapi(db.Model):
    __tablename__ = 'sapi'
    id = db.Column(db.Integer(), primary_key=True)
    no_sapi = db.Column(db.String(255), nullable=False)
    fitur1 = db.Column(db.Integer())
    fitur2 = db.Column(db.Integer())
    fitur3 = db.Column(db.Integer())
    laktasi = db.Column(db.Integer())
    ib = db.Column(db.DateTime, default=datetime.now)
    pkb = db.Column(db.DateTime, default=datetime.now)
    anggota_id = db.Column(db.Integer(), db.ForeignKey('anggota.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamps(), onupdate=db.func.current_timestamp())

    def __init__(self, no_sapi):
        self.no_sapi = no_sapi
    
    def __repr__(self):
        return '<nomor sapi : {}>'.format(self.no_sapi)
class AnggotaForm(Formulir):
    no_anggota = StringField('Nomor Anggota', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    namaanggota = StringField('Nama Anggota', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    kirim = SubmitField('Tambah')

class WilayahForm(Formulir):
    namawilayah = StringField('Nama Wilayah', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    kirim = SubmitField('Tambah')

class SapiForm(Formulir):
    no_sapi = StringField('Nomor Telinga', validators=[DataRequired(message='Tidak boleh kosong'), Length(max=30)])
    fitur1 = IntegerField('Fitur 1', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=10)])
    fitur2 = IntegerField('Fitur 2', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=10)])
    fitur3 = IntegerField('Fitur 3', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=10)])
    laktasi = IntegerField('Laktasi', validators=[DataRequired(message='Tidak boleh kosong'), NumberRange(min=1, max=4)])
    ib = DateField('IB ke-', id='ib')
    pkb = DateField('PKB', id='pkb')
    kirim = SubmitField('Tambah')

@apl.route('/wilayah', methods=('GET', 'POST'))
def addwilayah():
    fm = WilayahForm()
    if fm.validate_on_submit():
        pass
    return render_template('wilayah_add.html', title='Tambah Wilayah', fm=fm)

@apl.route('/anggota', methods=('GET', 'POST'))
def addanggota():
    fm = AnggotaForm()
    if fm.validate_on_submit():
        pass
    return render_template('anggota_add.html', title='Tambah Wilayah', fm=fm)
    
@apl.route('/sapi', methods=('GET', 'POST'))
def addsapi():
    fm = SapiForm()
    if fm.validate_on_submit():
        pass
    return render_template('sapi_add.html', title='Tambah Wilayah', fm=fm)
