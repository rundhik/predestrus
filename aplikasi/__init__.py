from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_login import current_user, login_required
from flask_admin import Admin
from datetime import datetime
from konfigurasi import DevConfig


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
moment = Moment()
adm = Admin()

def buat_app(nama_konfigurasi):
    
    apl = Flask(__name__)
    apl.config.from_object(nama_konfigurasi)

    db.init_app(apl)
    migrate.init_app(apl, db)
    bootstrap.init_app(apl)
    moment.init_app(apl)
    adm.init_app(apl)

    from .utama import buat_modul as induk_modul
    from .otentikasi import buat_modul as auth_modul
    from .wilayah import buat_modul as wilayah_modul
    from .anggota import buat_modul as anggota_modul
    from .sapi import buat_modul as sapi_modul
    
    induk_modul(apl)
    auth_modul(apl)
    wilayah_modul(apl)
    anggota_modul(apl)
    sapi_modul(apl)

    apl.register_error_handler(404, laman_tak_ditemukan)
    apl.register_error_handler(403, akses_ditolak)
    apl.register_error_handler(500, internal_error)

    @apl.before_request
    def before_request():
        if current_user.is_authenticated:
            current_user.last_login = datetime.utcnow()
            db.session.commit()
    
    return apl

def laman_tak_ditemukan(error):
    return render_template('/galat/404.html'), 404
def internal_error(error):
    db.session.rollback()
    return render_template('/galat/500.html'), 500
def akses_ditolak(error):
    return render_template('/galat/403.html'), 403

import functools

def has_role(name):
    def real_decorator(f):
        def wraps(*args, **kwargs):
            if current_user.has_role(name):
                return f(*args, **kwargs)
            else:
                abort(403)
        return functools.update_wrapper(wraps, f)
    return real_decorator