from flask import render_template, Blueprint, flash, redirect, url_for
from .pkb_models import db, Pkb
from .pkb_forms import PkbForm
from aplikasi import has_role, login_required
from datetime import date
from . import ModelView

pkb_bp = Blueprint(
    'pkbs',
    __name__,
    template_folder='../templates/pkb',
    url_prefix="/pkbs"
)

class PkbList(ModelView):
    column_searchable_list = ('id', 'inseminasi_id',)
    column_sortable_list = ('inseminasi_id', 'tgl_pkb',)

@pkb_bp.route('/', methods=('GET', 'POST'))
def index():
    q = Pkb.query.all()
    return render_template('pkb_index.html', title='Data Pemeriksaan Kebuntingan', data=q)

@pkb_bp.route('/add', methods=('GET', 'POST'))
def addpkb():
    fm = PkbForm()
    if fm.validate_on_submit():
        pkb = Pkb(inseminasi_id=fm.inseminasi.data)
        pkb.sem_code = fm.sem_code.data
        pkb.batch = fm.batch.data
        pkb.ib_hasil = fm.ib_hasil.data
        pkb.tgl_pkb = fm.tgl_pkb.data
        db.session.add(pkb)
        db.session.commit()
        flash('Data IB berhasi ditambahkan')
        return redirect(url_for('pkbs.index'))
    return render_template('pkb_add.html', title='Pemeriksaan Kebuntingan', fm=fm)