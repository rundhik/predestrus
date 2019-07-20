from .. import db
class Wilayah(db.Model):
    __tablename__ = 'wilayah'
    id = db.Column(db.Integer(), primary_key=True)
    namawilayah = db.Column(db.String(255), nullable=False, index=True)
    anggotas = db.relationship(
        'Anggota',
        backref='anggota',
        lazy='dynamic'
    )
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamps(), onupdate=db.func.current_timestamp())

    def __init__(self, namawilayah):
        self.namawilayah = namawilayah
    
    def __repr__(self):
        return '<wilayah : {}>'.format(self.namawilayah)