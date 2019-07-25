from flask import render_template, Blueprint, flash, redirect, url_for
from aplikasi import has_role, login_required, db, pd

ann_bp = Blueprint(
    'ann',
    __name__,
    template_folder='../templates/ann',
)

@ann_bp.route('/prediksi', methods=('GET', 'POST'))
def prediksi():
    s = []
    from sqlalchemy import text
    sql = text('select * from dataset')
    r = db.engine.execute(sql)
    for rpf, perilaku, ib_ke, jarak_ib, laktasi, ib_hasil in r :
        s.append((rpf, perilaku, ib_ke, jarak_ib, laktasi, ib_hasil))
    return render_template('prediksi.html', title='Prediksi', prediksi=s)

