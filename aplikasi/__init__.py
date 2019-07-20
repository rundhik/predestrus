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
    from .utama.controllers import induk_bp
    from .wilayah.wilayah_controllers import wilayah_bp
    from .anggota.anggota_controllers import anggota_bp
    from .sapi.sapi_controllers import sapi_bp
    
    apl = Flask(__name__)
    apl.config.from_object(aplikasiestrus)

    db.init_app(apl)
    migrate.init_app(apl, db)
    bootstrap.init_app(apl)
    moment.init_app(apl)

    apl.register_blueprint(wilayah_bp)
    apl.register_blueprint(induk_bp)
    apl.register_blueprint(anggota_bp)
    apl.register_blueprint(sapi_bp)
    apl.register_error_handler(404, laman_tak_ditemukan)

    return apl