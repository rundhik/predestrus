from .. import db
from datetime import date, datetime

class Inseminasi(db.Model):
    __tablename__ = 'sapi'
    id = db.Column(db.Integer(), primary_key=True)
    sapi_id = db.Column(db.Integer(), db.ForeignKey('sapi.id'))
    ibsapi = db.relationship('Sapi')
    sem_code = db.Column(db.String(20), nullable=False)
    batch = db.Column(db.String(20), nullable=False)
    rpf = db.Column(db.Integer())
    perilaku = db.Column(db.Integer())
    ib_ke = db.Column(db.Integer())
    jarak_ib = db.Column(db.Integer())
    laktasi = db.Column(db.Integer())
    tgl_ib = db.Column(db.Date, default=date.today)
    
    def __repr__(self):
        return '<IB sapi : {}>'.format(self.sapi_id)