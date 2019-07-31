from flask import render_template, Blueprint, flash, redirect, url_for
from .wilayah_models import db, Wilayah
from .wilayah_forms import WilayahForm
from aplikasi import has_role, login_required

wilayah_bp = Blueprint(
    'region',
    __name__,
    template_folder='../templates/wilayah',
    url_prefix="/region"
)

@wilayah_bp.route('/', methods=('GET', 'POST'))
def index():
    q = Wilayah.query.all()
    return render_template('wilayah_index.html', title='List Wilayah', data=q)

@wilayah_bp.route('/add', methods=('GET', 'POST'))
# @login_required
# @has_role('admin')
def addwilayah():
    fm = WilayahForm()
    if fm.validate_on_submit():
        pass
    return render_template('wilayah_add.html', title='Tambah Wilayah', fm=fm)