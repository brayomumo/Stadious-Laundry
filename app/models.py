from flask_security import UserMixin, RoleMixin

from . import db

# Define models

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    item = db.relationship('Item', backref='user', lazy='dynamic')
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,backref=db.backref('users', lazy='dynamic'))
    def __str__(self):
        return self.email
    
class Item (db.Model):

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    itemName = db.Column(db.String())
    itemPrice= db.Column(db.Integer())

    @classmethod

    def get_items(cls, id)
        items = Item.query.order_by(item_id=id).desc().all()
        return items

    def __repr__(self):
        return f'Item {self.itemName, itemPrice}'