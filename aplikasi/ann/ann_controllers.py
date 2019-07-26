from flask import render_template, Blueprint, flash, redirect, url_for
from aplikasi import has_role, login_required, db, pd
from aplikasi.sapi.sapi_models import Sapi, Prediksi

ann_bp = Blueprint(
    'ann',
    __name__,
    template_folder='../templates/ann',
)


@ann_bp.route('/prediksi', methods=('GET', 'POST'))
def prediksi():
    q = Sapi.query.all()
    from aplikasi.ann.ann_models import Classifier as cls
    if ( Prediksi.query.all() == []): #bulk insert (doing once when table is empty)
        for i in q:
            e = cls.mlp.predict([[i.rpf, i.perilaku, i.ib_ke, i.jarak_ib, i.laktasi]])
            d = Prediksi(
                sapi_id = i.id,
                estrus = int(e[0])
            )
            db.session.add(d)
    else:
        for i in q:
            e = cls.mlp.predict([[i.rpf, i.perilaku, i.ib_ke, i.jarak_ib, i.laktasi]])
            if Prediksi.query.filter_by(sapi_id=i.id) == i.id:
                Prediksi.query.filter_by(sapi_id=i.id).update(
                    Prediksi(estrus = e[0])
                )
            elif Prediksi.query.filter_by(sapi_id = i.id).all() == []:
                e = cls.mlp.predict([[i.rpf, i.perilaku, i.ib_ke, i.jarak_ib, i.laktasi]])
                f = Prediksi(sapi_id = i.id, estrus = int(e[0]))
                db.session.add(f)

    db.session.commit()
    data = Prediksi.query.all()
    return render_template('prediksi.html', title='Prediksi', prediksi=data)

