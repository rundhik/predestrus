from flask import render_template, Blueprint, flash, redirect, url_for
from .inseminasi_models import db, Inseminasi
# from .inseminasi_form import InseminasiForm
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