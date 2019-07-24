from aplikasi import db, adm
from flask_admin.contrib.sqla import ModelView
from aplikasi.inseminasi import inseminasi_models as mib
from aplikasi.inseminasi import inseminasi_controllers as cib


def buat_modul(apl, **kwargs):
    from .inseminasi_controllers import ib_bp
    apl.register_blueprint(ib_bp)
    adm.add_view(cib.InseminasiList(cib.Inseminasi, db.session))