from aplikasi import db, adm
from flask_admin.contrib.sqla import ModelView
from aplikasi.pkb import pkb_models as mpkb
from aplikasi.pkb import pkb_controllers as cpkb


def buat_modul(apl, **kwargs):
    from .pkb_controllers import pkb_bp
    apl.register_blueprint(pkb_bp)
    adm.add_view(cpkb.PkbList(cpkb.Pkb, db.session))