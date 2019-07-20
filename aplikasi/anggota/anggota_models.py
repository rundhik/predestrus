from .. import db

class Anggota(db.Model):
    __tablename__ = 'anggota'
    id = db.Column(db.Integer(), primary_key=True)
    no_anggota = db.Column(db.String(255))
    namaanggota = db.Column(db.String(255), nullable=False, index=True)
    wilayah = db.Column(db.Integer(), db.ForeignKey('wilayah.id'))
    sapis = db.relationship(
        'Sapi',
        backref='sapi',
        lazy='dynamic'
    )
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamps(), onupdate=db.func.current_timestamp())

    def __init__(self, namaanggota):
        self.namaanggota = namaanggota
    
    def __repr__(self):
        return '<nama anggota : {}>'.format(self.namaanggota)