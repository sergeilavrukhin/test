from flask_sqlalchemy import SQLAlchemy

# Init db
db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

# GroupUser relationship Table
groupuser = db.Table('groupuser',
    db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.UniqueConstraint('group_id', 'user_id', name='UC_group_id_user_id')
)

# Group Class/Model:
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    groupuser = db.relationship('User', secondary=groupuser, backref=db.backref("groupuser", lazy='dynamic'))

    def __init__(self, name):
        self.name = name

# User Class/Model:
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    subscribe = db.relationship("Subscribe", backref="recipient")

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Subscribe Class/Model:
class Subscribe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_send = db.Column(db.Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
