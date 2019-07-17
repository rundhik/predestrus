from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.relationship('Role', backref='id', lazy='dynamic')
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    created_at  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    
    def __init__(self, TimeStamp):
        t = TimeStamp
        return t

    def __repr__(self):
        return '<User {} pass {}>'.format(self.username, self.password_hash)
    
    def set_password(self, katasandi):
        self.password_hash = generate_password_hash(katasandi)
    
    def periksa_password(self, katasandi):
        return check_password_hash(self.password_hash, katasandi)

@login.user_loader
def muat_pengguna(id):
    return User.query.get(int(id))

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    user_id = db.relationship('User', backref='role', lazy='dynamic')
    
    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0
    
    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm
    
    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0
    
    def has_permission(self, perm):
        return self.permissions & perm == perm

class Permission:
    READ = 1
    SAPI = 2
    KELOMPOK = 4
    WILAYAH = 8
    ADMIN = 16
    USER = 32

@staticmethod
def insert_roles():
    roles = {
        'Anggota': [Permission.READ],
        'Ketua': [Permission.READ, Permission.SAPI, Permission.KELOMPOK],
        'Koordinator': [Permission.READ, Permission.SAPI, Permission.KELOMPOK, Permission.WILAYAH],
        'Administrator': [Permission.READ, Permission.SAPI,
        Permission.KELOMPOK, Permission.WILAYAH, Permission.ADMIN],
        'SuperUser': [Permission.READ, Permission.SAPI, Permission.KELOMPOK,
        Permission.WILAYAH, Permission.ADMIN, Permission.USER],
        }
    default_role = 'User'
    
    for r in roles:
        role = Role.query.filter_by(name=r).first()
        if role is None:
            role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
        db.session.add(role)
    db.session.commit()