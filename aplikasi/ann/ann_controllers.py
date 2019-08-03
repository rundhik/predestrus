from flask import render_template, Blueprint, flash, redirect, url_for
from aplikasi import has_role, login_required, db, pd
from aplikasi.sapi.sapi_models import Sapi, Prediksi
from aplikasi.ann import MinMaxScaler
from sqlalchemy import text

ann_bp = Blueprint(
    'ann',
    __name__,
    template_folder='../templates/ann',
)


@ann_bp.route('/prediksi', methods=('GET', 'POST'))
def prediksi():
    # db.engine.execute('DELETE FROM prediksi')
    # db.session.commit()
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
    x = 0
    y = 0
    for i in q:
        e = cls.mlp.predict([[
            (i.rpf - rpfmin)/(rpfmax-rpfmin), 
            (i.perilaku - perilakumin)/(perilakumax-perilakumin), 
            (i.ib_ke - ib_kemin)/(ib_kemax-ib_kemin), 
            ((i.jarak_ib+3) - jarak_ibmin)/(jarak_ibmax-jarak_ibmin), 
            (i.laktasi - laktasimin)/(laktasimax-laktasimin),
        ]])
        if Prediksi.query.filter_by(sapi_id = i.id).all() == []:
            f = Prediksi(sapi_id = i.id, estrus = int(e[0]))
            x = x + 1
            db.session.add(f)
            
        elif Prediksi.query.filter_by(sapi_id = i.id).first().sapi_id == i.id:
            Prediksi.query.filter_by(sapi_id=i.id).update({ 'estrus' : int(e[0])})
            y = y + 1
            db.session.commit()

    db.session.commit()
    db.session.close()
    data = Prediksi.query.all()
    # return render_template('prediksi.html', title='Prediksi', prediksi=data, x=x, y=y)
    return redirect(url_for('ann.hasil'))

@ann_bp.route('/hasilprediksi', methods=('GET', 'POST'))
def hasil():
    from sqlalchemy import text
    q = text('SELECT sapi.no_sapi as "sapi", anggota.namaanggota as "anggota", prediksi.estrus "estrus", date(prediksi.updated_at, "+3 days") as "tanggal", wilayah.namawilayah as "wilayah" FROM prediksi LEFT JOIN sapi ON sapi.id = prediksi.sapi_id LEFT JOIN anggota ON anggota.id = sapi.anggota_id LEFT JOIN wilayah ON wilayah.id = anggota.wilayah_id WHERE prediksi.estrus = 1')
    r = db.engine.execute(q)
    data = []
    for sapi, anggota, estrus, tanggal, wilayah in r:
        data.append((sapi,anggota, estrus, tanggal, wilayah))
    
    from aplikasi.ann.ann_models import Classifier as cls
    acc = cls.mlp_score
    roc = cls.roc_score
    cm = cls.cm
    return render_template('hasil.html', title='Hasil Prediksi', prediksi=data, akurasi=acc, roc=roc, cm=cm)