import sqlalchemy as sa
import pandas as pd
from .. import db
from . import (
    np, pd, train_test_split, MinMaxScaler,
    accuracy_score, cohen_kappa_score, MLPClassifier,
    roc_auc_score, confusion_matrix
)

def getDataset(tabel='dataset'):
    df = pd.read_sql_table(tabel, db.engine)
    return df

#call from aplikasi.ann import ann_models as ann
# def tts(ts=0.2):
    
#     # x_train = Split(x_train)
#     # x_test = Split(x_test)
#     # y_train = Split(y_train)
#     # y_test = Split(y_test)
#     return x_train, x_test, y_train, y_test

class Split:
    df = getDataset()
    df.columns = range(df.shape[1])
    x =  df.loc[:,len(df.columns)-len(df.columns):len(df.columns)-2]
    y = df.loc[:,len(df.columns)-1:len(df.columns)-1]
    x_train, x_test, y_train, y_test = train_test_split(x,y, 
                                                    test_size=.2, 
                                                    random_state=1)
    def xtrain(self, x_train):
        return self.x_train
    def xtest(self, x_test):
        return self.x_test
    def ytrain(self, y_train):
        return self.y_train
    def ytest(self, y_test):
        return self.y_test