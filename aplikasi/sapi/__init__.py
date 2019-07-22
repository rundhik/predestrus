from aplikasi import db, adm
from flask_admin.contrib.sqla import ModelView
import aplikasi.sapi.sapi_models as msapi


def buat_modul(apl, **kwargs):
    from .sapi_controllers import sapi_bp
    apl.register_blueprint(sapi_bp)
    adm.add_view(ModelView(msapi.Sapi, db.session))
    