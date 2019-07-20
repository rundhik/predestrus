from .. import db
from datetime import datetime
from sqlalchemy import func

class Sapi(db.Model):
    __tablename__ = 'sapi'
    id = db.Column(db.Integer(), primary_key=True)
    no_sapi = db.Column(db.String(255), nullable=False)
    fitur1 = db.Column(db.Integer())
    fitur2 = db.Column(db.Integer())
    fitur3 = db.Column(db.Integer())
    laktasi = db.Column(db.Integer())
    ib = db.Column(db.DateTime, default=datetime.now)
    pkb = db.Column(db.DateTime, default=datetime.now)
    anggota_id = db.Column(db.Integer(), db.ForeignKey('anggota.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamps(), onupdate=db.func.current_timestamp())

    def __init__(self, no_sapi):
        self.no_sapi = no_sapi
    
    def __repr__(self):
        return '<nomor sapi : {}>'.format(self.no_sapi)