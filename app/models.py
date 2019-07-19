from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

users_roles = db.Table(
    'role_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref=db.backref('users', lazy='dynamic')
    )
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    created_at  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    # def __init__(self, username=""):
    #     default = Role.query.filter_by(name="default").one()
    #     self.roles.append(default)
    #     self.username = username

    def __repr__(self):
        return '<User {} pass {}>'.format(self.username, self.password_hash)
    
    def set_password(self, katasandi):
        self.password_hash = generate_password_hash(katasandi)
    
    def periksa_password(self, katasandi):
        return check_password_hash(self.password_hash, katasandi)
    
    def add_role(self, role):
        self.roles.append(role)

    def add_roles(self, roles):
        for role in roles:
            self.add_role(role)

    def has_role(self, name):
        for role in self.roles:
            if role.name == name:
                return True
            return False

@login.user_loader
def muat_pengguna(id):
    return User.query.get(int(id))

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<Role {}'.format(self.name)

    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()