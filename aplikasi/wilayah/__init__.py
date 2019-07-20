def buat_modul(apl, **kwargs):
    from .wilayah_controllers import wilayah_bp
    apl.register_blueprint(wilayah_bp)