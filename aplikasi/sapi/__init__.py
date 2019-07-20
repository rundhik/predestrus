def buat_modul(apl, **kwargs):
    from .sapi_controllers import sapi_bp
    apl.register_blueprint(sapi_bp)