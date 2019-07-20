def buat_modul(apl, **kwargs):
    from .controllers import induk_bp
    apl.register_blueprint(induk_bp)