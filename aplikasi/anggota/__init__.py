def buat_modul(apl, **kwargs):
    from .anggota_controllers import anggota_bp
    apl.register_blueprint(anggota_bp)