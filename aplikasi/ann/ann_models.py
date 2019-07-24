import sqlalchemy as sa
import pandas as pd
from .. import db

def getDataset(tabel):
    df = pd.read_sql_table(tabel, db.engine)
    return df
