from aplikasi import db, adm
from flask_admin.contrib.sqla import ModelView
from aplikasi.wilayah import wilayah_models as mwilayah


def buat_modul(apl, **kwargs):
    from .wilayah_controllers import wilayah_bp
    apl.register_blueprint(wilayah_bp)
    adm.add_view(ModelView(mwilayah.Wilayah, db.session))