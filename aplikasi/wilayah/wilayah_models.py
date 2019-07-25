from aplikasi import db
from datetime import date, datetime

class Wilayah(db.Model):
    __tablename__ = 'wilayah'
    id = db.Column(db.Integer(), primary_key=True)
    namawilayah = db.Column(db.String(255), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return 'Wilayah : {}'.format(self.namawilayah)