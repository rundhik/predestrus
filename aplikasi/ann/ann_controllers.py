from flask import render_template, Blueprint, flash, redirect, url_for
from .ann_models import db, Classifier, Dataset
from aplikasi.ann import ann_models as mann
from aplikasi import has_role, login_required
from datetime import date
from . import ModelView

ann_bp = Blueprint(
    'ann',
    __name__,
    template_folder='../templates/ann',
)

@ann_bp.route('/prediksi', methods=('GET', 'POST'))
def prediksi():
    Classifier()
    df = mann.getDataset() #ujicoba pakai tabel dataset, nanti ambil dari tabel sapi
    df = df.values #convert panda dataframe jadi array
    for i in df:        
        df[i][5] = Classifier.mlp.predict(
            [[
                df[i][0],
                df[i][1],
                df[i][2],
                df[i][3],
                df[i][4]
            ]]
        )
    return render_template('prediksi.html', title='Prediksi', prediksi=df)

class PrediksiList(ModelView):
    column_searchable_list = ('id', 'inseminasi_id',)
    column_sortable_list = ('inseminasi_id', 'tgl_pkb',)

    # Coba skrip di flask shell
    # Classifier.mlp.predict(
    #         [[
    #             dt[153][0],
    #             dt[153][1],
    #             dt[153][2],
    #             dt[153][3],
    #             dt[153][4]
    #         ]]
    #     )