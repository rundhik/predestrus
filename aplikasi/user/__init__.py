from aplikasi import db, adm
from flask_admin.contrib.sqla import ModelView
from aplikasi.user import user_models as muser
from aplikasi.user import user_controllers as cuser

# adm.add_view(ModelView(muser.User, db.session))
adm.add_view(cuser.UserAdminView(cuser.User, db.session))

def buat_modul(apl, **kwargs):
    from .user_controllers import pengguna_bp
    apl.register_blueprint(pengguna_bp)
    