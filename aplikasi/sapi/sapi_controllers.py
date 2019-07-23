from flask import render_template, Blueprint, flash, redirect, url_for
from .sapi_models import db, Sapi
from .sapi_forms import SapiForm
from aplikasi import has_role, login_required
from datetime import date
from . import ModelView

sapi_bp = Blueprint(
    'cow',
    __name__,
    template_folder='../templates/sapi',
    url_prefix="/cow"
)

class SapiList(ModelView):
    column_searchable_list = ('no_sapi', 'anggota_id',)
    column_sortable_list = ('no_sapi',)
    column_exclude_list = ('created_at', 'updated_at')
# @sapi_bp.route('/', methods=('GET', 'POST'))
# @login_required
# @has_role('petugas')
# def addsapi():
#     fm = SapiForm()
#     if fm.validate_on_submit():
#         s = Sapi(no_sapi=fm.no_sapi.data)
#         s.fitur1 = fm.fitur1.data
#         s.fitur2 = fm.fitur2.data
#         s.fitur3 = fm.fitur3.data
#         s.laktasi = fm.laktasi.data
#         s.ib = fm.ib.data
#         s.pkb = fm.pkb.data
#         db.session.add(s)
#         db.session.commit()
#         flash('Data sapi berhasi ditambahkan')
#         return redirect(url_for('induk.home'))
#     return render_template('sapi_add.html', title='Inseminasi Buatan', fm=fm)