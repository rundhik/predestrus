import os
from aplikasi import buat_app, db, migrate
from aplikasi.user.user_models import User, Role
from aplikasi.wilayah.wilayah_models import Wilayah
from aplikasi.anggota.anggota_models import Anggota
from aplikasi.sapi.sapi_models import Sapi, Prediksi
from aplikasi.inseminasi.inseminasi_models import Inseminasi
from aplikasi.pkb.pkb_models import Pkb

env = os.environ.get('WEBAPP_ENV', 'dev')
apl = buat_app('konfigurasi.%sConfig' % env.capitalize())

@apl.shell_context_processor
def make_shell_context():
    return dict(
        apl=apl, 
        db=db, 
        migrate=migrate,
        Wilayah=Wilayah,
        Anggota=Anggota,
        Sapi=Sapi,
        User=User,
        Role=Role,
        Inseminasi=Inseminasi,
        Pkb=Pkb,
        Prediksi=Prediksi
        )

if __name__ == '__main__':
    apl.run()