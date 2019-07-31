from aplikasi import db
from datetime import date, datetime

class Pkb(db.Model):
    __tablename__ = 'pkb'
    id = db.Column(db.Integer(), primary_key=True)
    inseminasi_id = db.Column(db.Integer(), db.ForeignKey('inseminasi.id'))
    inseminasi = db.relationship('Inseminasi')
    sem_code = db.Column(db.String(20), nullable=False)
    batch = db.Column(db.String(20), nullable=False)
    ib_hasil = db.Column(db.Integer())
    tgl_pkb = db.Column(db.Date, default=date.today)
    
    def __repr__(self):
        return 'PKB sapi IB : {}'.format(self.inseminasi_id)