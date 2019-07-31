from flask import render_template, Blueprint, flash, redirect, url_for
from .pkb_models import db, Pkb
# from .inseminasi_form import InseminasiForm
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