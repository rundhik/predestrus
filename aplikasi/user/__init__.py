from aplikasi import db, adm
from flask_admin.contrib.sqla import ModelView
import aplikasi.user.user_models as muser
import aplikasi.user.user_controllers as cuser

# adm.add_view(ModelView(muser.User, db.session))
adm.add_view(cuser.UserAdminView(cuser.User, db.session))

def buat_modul(apl, **kwargs):
    from .user_controllers import pengguna_bp
    apl.register_blueprint(pengguna_bp)
    