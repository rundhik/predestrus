from flask import render_template, Blueprint, flash, redirect, url_for
from .inseminasi_models import db, Inseminasi
from .inseminasi_forms import InseminasiForm
from aplikasi import has_role, login_required
from datetime import date
from . import ModelView

ib_bp = Blueprint(
    'ib',
    __name__,
    template_folder='../templates/inseminasi',
    url_prefix="/ib"
)

class InseminasiList(ModelView):
    column_searchable_list = ('id', 'sapi_id',)
    column_sortable_list = ('sapi_id', 'tgl_ib',)

@ib_bp.route('/', methods=('GET', 'POST'))
def index():
    q = Inseminasi.query.all()
    return render_template('inseminasi_index.html', title='Inseminasi Buatan', data=q)

@ib_bp.route('/add', methods=('GET', 'POST'))
def addib():
    fm = InseminasiForm()
    if fm.validate_on_submit():
        ib = Inseminasi(sapi_id=fm.sapi.data)
        ib.sem_code = fm.sem_code.data
        ib.batch = fm.batch.data
        ib.rpf = fm.rpf.data
        ib.perilaku = fm.perilaku.data
        ib.ib_ke = fm.ib_ke.data
        ib.jarak_ib = fm.jarak_ib.data
        ib.laktasi = fm.laktasi.data
        db.session.add(ib)
        db.session.commit()
        flash('Data IB berhasi ditambahkan')
        return redirect(url_for('ib.index'))
    return render_template('inseminasi_add.html', title='Inseminasi Buatan', fm=fm)