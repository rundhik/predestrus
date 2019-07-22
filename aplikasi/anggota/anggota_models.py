from .. import db
from datetime import date, datetime

class Anggota(db.Model):
    __tablename__ = 'anggota'
    id = db.Column(db.Integer(), primary_key=True)
    no_anggota = db.Column(db.String(255))
    namaanggota = db.Column(db.String(255), nullable=False, index=True)
    wilayah_id = db.Column(db.Integer(), db.ForeignKey('wilayah.id'))
    wilayah = db.relationship('Wilayah')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<nama anggota : {}>'.format(self.namaanggota)