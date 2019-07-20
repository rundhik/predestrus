from flask import render_template, Blueprint, flash, redirect, url_for
from .wilayah_models import db, Wilayah
from .wilayah_forms import WilayahForm

wilayah_bp = Blueprint(
    'wilayah',
    __name__,
    template_folder='../templates/wilayah',
    url_prefix="/wilayah"
)

@wilayah_bp.route('/', methods=('GET', 'POST'))
def addwilayah():
    fm = WilayahForm()
    if fm.validate_on_submit():
        pass
    return render_template('wilayah_add.html', title='Tambah Wilayah', fm=fm)