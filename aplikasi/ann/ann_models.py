from aplikasi import db, pd
from aplikasi.ann import (
    train_test_split, MinMaxScaler,
    accuracy_score, cohen_kappa_score, MLPClassifier,
    roc_auc_score, confusion_matrix, resample, confusion_matrix
)
from datetime import date, datetime
from aplikasi.sapi.sapi_models import Sapi

def getDataset():
        df = pd.read_sql_table('dataset', db.engine)
        return df

# class Original:
#     df = pd.read_sql_table('dataset', db.engine)
#     df.columns = range(df.shape[1])
#     x =  df.loc[:,len(df.columns)-len(df.columns):len(df.columns)-2]
#     y = df.loc[:,len(df.columns)-1:len(df.columns)-1]
#     x_train, x_test, y_train, y_test = train_test_split(x,y, 
#                                                     test_size=.2, 
#                                                     random_state=1)
#     def xtrain(self, x_train):
#         return self.x_train
#     def xtest(self, x_test):
#         return self.x_test
#     def ytrain(self, y_train):
#         return self.y_train
#     def ytest(self, y_test):
#         return self.y_test
# db = db.engine
# df = pd.read_sql_table('dataset', db)

class Oversampling:
    df = getDataset()
    df.columns = range(df.shape[1])
    x =  df.loc[:,len(df.columns)-len(df.columns):len(df.columns)-2]
    y = df.loc[:,len(df.columns)-1:len(df.columns)-1]
    # value = y.value_counts()
    major = y.loc[:,5].value_counts()[1]
    minor = y.loc[:,5].value_counts()[0]
    df_majority = df[df.loc[:,5]==1]
    df_minority = df[df.loc[:,5]==0]

    # Upsample minority class (Oversampling)
    df_minority_upsampled = resample(df_minority, 
                                   replace=True, # sample with replacement
                                   n_samples=major,  # to match majority class
                                   random_state=123) # reproducible results
    # Combine majority class with upsampled minority class
    df = pd.concat([df_majority, df_minority_upsampled])

    x =  df.loc[:,len(df.columns)-len(df.columns):len(df.columns)-2]
    y = df.loc[:,len(df.columns)-1:len(df.columns)-1]
    value = y.loc[:,5].value_counts()
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
    def val(self, value):
        return self.value

class Undersampling:
    df = getDataset()
    df.columns = range(df.shape[1])
    x =  df.loc[:,len(df.columns)-len(df.columns):len(df.columns)-2]
    y = df.loc[:,len(df.columns)-1:len(df.columns)-1]
    
    major = y.loc[:,5].value_counts()[1]
    minor = y.loc[:,5].value_counts()[0]
    df_majority = df[df.loc[:,5]==1]
    df_minority = df[df.loc[:,5]==0]

    # Downsample majority class (Undersampling)
    df_majority_downsampled = resample(df_majority, 
                                    replace=False,    # sample without replacement
                                    n_samples=minor,     # to match minority class
                                    random_state=123) # reproducible results
    # Combine minority class with downsampled majority class
    df = pd.concat([df_majority_downsampled, df_minority])

    x =  df.loc[:,len(df.columns)-len(df.columns):len(df.columns)-2]
    y = df.loc[:,len(df.columns)-1:len(df.columns)-1]
    value = y.loc[:,5].value_counts()
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
    def val(self, value):
        return self.value

class Classifier:
    xtr = MinMaxScaler().fit_transform(Oversampling.x_train)
    ytr = Oversampling.y_train
    mlp = MLPClassifier(hidden_layer_sizes=(6,8,6), 
                    max_iter=300,
                    activation='tanh',
                    random_state=1,
                    solver='lbfgs',
                    verbose=10,
                    warm_start=False
                    )
    mlp.fit(xtr, ytr)

    xts = MinMaxScaler().fit_transform(Oversampling.x_test)
    yts = Oversampling.y_test
    y_pred = mlp.predict(xts)
    mlp_score = mlp.score(xts, yts)
    roc_score = roc_auc_score(yts, y_pred)
    cm = confusion_matrix(yts, y_pred)

    def cls(self, mlp):
        return self.mlp
    def mlpscore(self, mlp_score):
        return self.mlp_score
    def rocscore(self, roc_score):
        return self.roc_score
    def cfm(self, cm):
        return self.cm

class Prediction:
    s = Sapi.query.all()

    pass