from flask import render_template, Blueprint, flash, redirect, url_for
from aplikasi import has_role, login_required, db, pd

ann_bp = Blueprint(
    'ann',
    __name__,
    template_folder='../templates/ann',
)

@ann_bp.route('/prediksi', methods=('GET', 'POST'))
def prediksi():
    from .ann_models import Classifier
    cls = Classifier()
    df = pd.read_sql_table('dataset', db.engine)
    #ujicoba pakai tabel dataset, nanti ambil dari tabel sapi
    df = df.values #convert panda dataframe jadi array
    for i in df:        
        df[i][5] = cls.mlp.predict(
            [[
                df[i][0],
                df[i][1],
                df[i][2],
                df[i][3],
                df[i][4]
            ]]
        )
    return render_template('prediksi.html', title='Prediksi', prediksi=df)

