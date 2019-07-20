import os
from aplikasi import buat_app

env = os.environ.get('WEBAPP_ENV', 'dev')
apl = buat_app('konfigurasi.%sConfig' % env.capitalize())

if __name__ == '__main__':
    apl.run()