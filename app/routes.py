from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import MasukForm, DaftarForm
from app.models import User
from app import app, db
from werkzeug.urls import url_parse
from datetime import datetime

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_login = datetime.utcnow()
        db.session.commit()

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author' : {'username': 'John'},
            'body' : 'Beautiful day in Portland'
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def masuk():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = MasukForm()
    if form.validate_on_submit():
        pengguna = User.query.filter_by(username=form.namauser.data).first()
        if pengguna is None or not pengguna.periksa_password(form.katasandi.data):
            flash('Pengguna atau Password salah')
            return redirect(url_for('masuk'))
        login_user(pengguna, remember=form.ingat_saya.data)
        flash('Login Sukses')
        laman_selanjutnya = request.args.get('next')
        if not laman_selanjutnya or url_parse(laman_selanjutnya).netloc != '':
            laman_selanjutnya = url_for('index')
        return redirect(laman_selanjutnya)
    return render_template('login.html', title='Masuk', fm=form)

@app.route('/logout')
def keluar():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def daftar():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = DaftarForm()
    if form.validate_on_submit():
        pengguna = User(username=form.namauser.data, email=form.surel.data)
        pengguna.set_password(form.katasandi.data)
        db.session.add(pengguna)
        db.session.commit()
        flash('Anda berhasil terdaftar')
        return redirect(url_for('masuk'))
    return render_template('register.html', title='Daftar', fm=form)