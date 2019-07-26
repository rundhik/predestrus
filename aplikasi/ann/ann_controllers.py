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
    # from aplikasi.ann.ann_models import Classifier as cls
    if ( Prediksi.query.all() == []): #bulk insert (doing once when table is empty)
        for i in q:
            d = Prediksi(
                sapi_id = i.id,
                estrus = 44
            )
            db.session.add(d)
    else:
        for i in q:
            if Prediksi.query.filter_by(sapi_id=i.id) == i.id:
                Prediksi.query.filter_by(sapi_id=i.id).update(
                    {
                        Prediksi.estrus : 55
                    }
                )
            elif Prediksi.query.filter_by(sapi_id = i.id).all() == []:
                f = Prediksi(sapi_id = i.id, estrus = 66)
                db.session.add(f)

    db.session.commit()
    data = Prediksi.query.all()
    return render_template('prediksi.html', title='Prediksi', prediksi=data)

