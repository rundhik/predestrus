from flask import render_template, Blueprint, flash, redirect, url_for
from aplikasi import login_required

induk_bp = Blueprint(
    'induk',
    __name__,
    template_folder='../templates/utama',
    url_prefix="/"
)

@induk_bp.route('/')
@login_required
def home():
    return render_template('home.html')