from aplikasi import db, adm
from flask_admin.contrib.sqla import ModelView
import aplikasi.user.user_models as muser

adm.add_view(ModelView(muser.User, db.session))

def buat_modul(apl, **kwargs):
    from .user_controllers import user_bp
    apl.register_blueprint(user_bp)
    