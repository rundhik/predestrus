from flask_login import LoginManager
from flask_bcrypt import Bcrypt

login_manager = LoginManager()
login_manager.login_view = "auth.masuk"
login_manager.login_message = "Silahkan login dahulu"
login_manager.login_message_category = "info"
bcrypt = Bcrypt()

@login_manager.user_loader
def load_user(id):
    from aplikasi.user.user_models import User
    return User.query.get(id)

def buat_modul(apl, **kwargs):
    login_manager.init_app(apl)
    bcrypt.init_app(apl)

    from .auth_controllers import auth_bp
    apl.register_blueprint(auth_bp)