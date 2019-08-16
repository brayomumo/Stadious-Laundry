from flask_security import UserMixin, RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_admin.contrib import sqla
from flask_admin import BaseView, expose
# Define models




class User(db.Model, UserMixin):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), index = True)
    password_hash = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))    
    
    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.username}'

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __str__(self):
        return self.name

class MicroBlogModelView(sqla.ModelView):
    
    def is_accessible(self):
        return login.current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))

    
# class Item (db.Model,UserMixin):
#     __tablename__ = "items"
#     id = db.Column(db.Integer, primary_key=True)
#     owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     itemName = db.Column(db.String())
#     itemPrice= db.Column(db.Integer())
# @classmethod
# def get_items(cls,id):
#     items = Item.query.order_by(item_id=id).desc().all()
#     return items
# def __repr__(self):
#     return f'Item {self.itemName, itemPrice}'
