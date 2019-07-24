from flask import render_template, Blueprint, flash, redirect, url_for
from .inseminasi_models import db, Inseminasi
# from .inseminasi_form import InseminasiForm
from aplikasi import has_role, login_required
from datetime import date

ib_bp = Blueprint(
    'inseminasi',
    __name__,
    template_folder='../templates/inseminasi',
    url_prefix="/inseminasi"
)