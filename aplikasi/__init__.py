from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
moment = Moment()

def buat_app(aplikasiestrus):
    
    apl = Flask(__name__)
    apl.config.from_object(aplikasiestrus)

    db.init_app(apl)
    migrate.init_app(apl, db)
    bootstrap.init_app(apl)
    moment.init_app(apl)

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

    return apl

def laman_tak_ditemukan(error):
    return render_template('/galat/404.html'), 404
def internal_error(error):
    db.session.rollback()
    return render_template('/galat/500.html'), 500
def akses_ditolak(error):
    return render_template('/galat/403.html'), 403