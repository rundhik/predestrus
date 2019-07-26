from flask import render_template, Blueprint, flash, redirect, url_for
from aplikasi import has_role, login_required, db, pd
from aplikasi.sapi.sapi_models import Sapi, Prediksi
from aplikasi.ann.ann_models import Classifier as cls

ann_bp = Blueprint(
    'ann',
    __name__,
    template_folder='../templates/ann',
)


@ann_bp.route('/prediksi', methods=('GET', 'POST'))
def prediksi():
    q = Sapi.query.all()
    if ( Prediksi.query.all() is None): #bulk insert (doing once when table is empty)
        for i in q:
            d = Prediksi(
                sapi_id = i.id, 
                estrus = cls.mlp.predict(
                    [[
                        i.rpf, i.perilaku, i.ib_ke, i.jarak_ib, i.laktasi
                    ]]
                ))
            db.session.add(d)
    else:
        for i in q:
            if ( Sapi.query.filter_by(sapi_id = i.id) is None ):
                d = Prediksi(
                sapi_id = i.id, 
                estrus = cls.mlp.predict(
                    [
                        [
                            i.rpf, i.perilaku, i.ib_ke, i.jarak_ib, i.laktasi
                        ]
                    ]
                ))
                db.session.add(d)
            else :
                e = cls.mlp.predict(
                    [
                        [
                            i.rpf, i.perilaku, i.ib_ke, i.jarak_ib, i.laktasi
                        ]
                    ]
                )
                d = Prediksi.query.filter_by(sapi_id = i.id).update(
                    {
                        Prediksi.estrus : e
                    }
                )
    
    db.session.commit()
    
    s = []
    from sqlalchemy import text
    sql = text('select * from prediksi')
    r = db.engine.execute(sql)
    for sapi_id, estrus in r :
        s.append((sapi_id, estrus))
    return render_template('prediksi.html', title='Prediksi', prediksi=s)

