def buat_modul(apl, **kwargs):
    from .user_controllers import user_bp
    apl.register_blueprint(user_bp)