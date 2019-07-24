from aplikasi import db, adm
from flask_admin.contrib.sqla import ModelView
from aplikasi.ann import ann_controllers as cann
from flask_sqlalchemy import BaseQuery


def buat_modul(apl, **kwargs):
    from .ann_controllers import ann_bp
    apl.register_blueprint(ann_bp)
    adm.add_view(cann.PrediksiList(cann.dataset, db.session))