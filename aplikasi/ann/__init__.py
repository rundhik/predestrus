import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, cohen_kappa_score,
    classification_report, confusion_matrix, roc_auc_score
)
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.preprocessing import MinMaxScaler
from aplikasi import db, adm
from flask_admin.contrib.sqla import ModelView
from aplikasi.ann import ann_controllers as cann
from aplikasi.ann import ann_models as mann


def buat_modul(apl, **kwargs):
    from .ann_controllers import ann_bp
    apl.register_blueprint(ann_bp)
    adm.add_view(cann.PrediksiList(cann.dataset, db.session))