from flask import render_template, Blueprint, flash, redirect, url_for
from .anggota_models import db, Anggota
from .anggota_forms import AnggotaForm
from aplikasi import has_role, login_required
from . import ModelView

anggota_bp = Blueprint(
    'member',
    __name__,
    template_folder='../templates/anggota',
    url_prefix="/member"
)

class AnggotaList(ModelView):
    column_searchable_list = ('namaanggota',)
    column_sortable_list = ('namaanggota',)
    column_exclude_list = ('created_at', 'updated_at')

# @anggota_bp.route('/', methods=('GET', 'POST'))
# @login_required
# @has_role('admin')
# def addanggota():
#     fm = AnggotaForm()
#     if fm.validate_on_submit():
#         pass
#     return render_template('anggota_add.html', title='Tambah Anggota', fm=fm)