from flask import render_template, Blueprint, flash, redirect, url_for
from .ann_models import db
from aplikasi import has_role, login_required
from datetime import date
from . import ModelView

ann_bp = Blueprint(
    'ann',
    __name__,
    template_folder='../templates/ann',
    url_prefix="/ann"
)

class PrediksiList(ModelView):
    column_searchable_list = ('id', 'inseminasi_id',)
    column_sortable_list = ('inseminasi_id', 'tgl_pkb',)