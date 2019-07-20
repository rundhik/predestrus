from flask import render_template, Blueprint, flash, redirect, url_for
from .anggota_models import db, Anggota
from .anggota_forms import AnggotaForm

anggota_bp = Blueprint(
    'anggota',
    __name__,
    template_folder='../templates/anggota',
    url_prefix="/anggota"
)

@anggota_bp.route('/', methods=('GET', 'POST'))
def addanggota():
    fm = AnggotaForm()
    if fm.validate_on_submit():
        pass
    return render_template('anggota_add.html', title='Tambah Anggota', fm=fm)