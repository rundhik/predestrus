from flask import render_template, Blueprint, flash, redirect, url_for
from .sapi_models import db, Sapi
from .sapi_forms import SapiForm
from aplikasi import has_role, login_required

sapi_bp = Blueprint(
    'sapi',
    __name__,
    template_folder='../templates/sapi',
    url_prefix="/sapi"
)

@sapi_bp.route('/', methods=('GET', 'POST'))
@login_required
@has_role('petugas')
def addsapi():
    fm = SapiForm()
    if fm.validate_on_submit():
        pass
    return render_template('sapi_add.html', title='Inseminasi Buatan', fm=fm)