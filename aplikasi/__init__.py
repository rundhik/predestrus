from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
moment = Moment()
def laman_tak_ditemukan(error):
    return render_template('404.html'), 404

def buat_app(aplikasiestrus):
    from .utama import buat_modul as induk_modul
    from .wilayah import buat_modul as wilayah_modul
    from .anggota import buat_modul as anggota_modul
    from .sapi import buat_modul as sapi_modul
    
    apl = Flask(__name__)
    apl.config.from_object(aplikasiestrus)

    db.init_app(apl)
    migrate.init_app(apl, db)
    bootstrap.init_app(apl)
    moment.init_app(apl)

    wilayah_modul(apl)
    induk_modul(apl)
    anggota_modul(apl)
    sapi_modul(apl)
    apl.register_error_handler(404, laman_tak_ditemukan)

    return apl