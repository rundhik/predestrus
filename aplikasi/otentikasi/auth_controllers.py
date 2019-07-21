from flask import render_template, Blueprint, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from werkzeug.urls import url_parse
from aplikasi.user.user_models import db, User
from .auth_forms import MasukForm, DaftarForm

auth_bp = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/otentikasi',
)

@auth_bp.route('/masuk', methods=('GET', 'POST'))
def masuk():
    if current_user.is_authenticated:
        return redirect(url_for('induk.home'))
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
            laman_selanjutnya = url_for('induk.home')
        return redirect(laman_selanjutnya)
    return render_template('masuk.html', title='Masuk', fm=form)

@auth_bp.route('/daftar', methods=('GET', 'POST'))
def daftar():
    if current_user.is_authenticated:
        return redirect(url_for('induk.home'))
    form = DaftarForm()
    if form.validate_on_submit():
        pengguna = User(username=form.namauser.data)
        pengguna.set_password(form.katasandi.data)
        db.session.add(pengguna)
        db.session.commit()
        flash('Anda berhasil terdaftar')
        return redirect(url_for('auth.masuk'))
    return render_template('daftar.html', title='Daftar', fm=form)

@auth_bp.route('/keluar')
def keluar():
    logout_user()
    return redirect(url_for('induk.home'))