from flask import render_template, Blueprint, flash, redirect, url_for
from aplikasi import has_role, login_required, db, pd
from aplikasi.sapi.sapi_models import Sapi, Prediksi
from aplikasi.ann import MinMaxScaler

ann_bp = Blueprint(
    'ann',
    __name__,
    template_folder='../templates/ann',
)


@ann_bp.route('/prediksi', methods=('GET', 'POST'))
def prediksi():
    q = Sapi.query.all()
    rpfmin = min(Sapi.query.with_entities(Sapi.rpf).all())[0]
    rpfmax = max(Sapi.query.with_entities(Sapi.rpf).all())[0]
    perilakumin = min(Sapi.query.with_entities(Sapi.perilaku).all())[0]
    perilakumax = max(Sapi.query.with_entities(Sapi.perilaku).all())[0]
    ib_kemin = min(Sapi.query.with_entities(Sapi.ib_ke).all())[0]
    ib_kemax = max(Sapi.query.with_entities(Sapi.ib_ke).all())[0]
    jarak_ibmin = min(Sapi.query.with_entities(Sapi.jarak_ib).all())[0]
    jarak_ibmax = max(Sapi.query.with_entities(Sapi.jarak_ib).all())[0]
    laktasimin = min(Sapi.query.with_entities(Sapi.laktasi).all())[0]
    laktasimax = max(Sapi.query.with_entities(Sapi.laktasi).all())[0]
    from aplikasi.ann.ann_models import Classifier as cls
    for i in q:
        e = cls.mlp.predict([[
            (i.rpf - rpfmin)/(rpfmax-rpfmin), 
            (i.perilaku - perilakumin)/(perilakumax-perilakumin), 
            (i.ib_ke - ib_kemin)/(ib_kemax-ib_kemin), 
            (i.jarak_ib - jarak_ibmin)/(jarak_ibmax-jarak_ibmin), 
            (i.laktasi - laktasimin)/(laktasimax-laktasimin),
        ]])
        if Prediksi.query.filter_by(sapi_id = i.id).all() == []:
            f = Prediksi(sapi_id = i.id, estrus = int(e[0]))
            db.session.add(f)        
        elif Prediksi.query.filter_by(sapi_id=i.id).all() == i.id:
            Prediksi.query.filter_by(sapi_id=i.id).update(
                Prediksi(estrus = int(e[0]))
            )
    db.session.commit()
    
    data = Prediksi.query.all()
    return render_template('prediksi.html', title='Prediksi', prediksi=data)

