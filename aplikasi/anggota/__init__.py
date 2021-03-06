from aplikasi import db, adm
from flask_admin.contrib.sqla import ModelView
from aplikasi.anggota import anggota_models as manggota
from aplikasi.anggota import anggota_controllers as canggota



def buat_modul(apl, **kwargs):
    from .anggota_controllers import anggota_bp
    apl.register_blueprint(anggota_bp)
    # adm.add_view(ModelView(manggota.Anggota, db.session))
    adm.add_view(canggota.AnggotaList(canggota.Anggota, db.session))