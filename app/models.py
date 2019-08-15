from flask_security import UserMixin, RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash
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
    username = db.Column(db.String(255), index = True)
    password_hash = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,backref=db.backref('users', lazy='dynamic'))
    
    def __str__(self):
        return self.email

# class User(db.Model, UserMixin):

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(255))
#     last_name = db.Column(db.String(255))
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(255))
#     active = db.Column(db.Boolean())
#     # item = db.relationship('Item', backref='user', lazy='dynamic')
#     confirmed_at = db.Column(db.DateTime())
#     roles = db.relationship('Role', secondary=roles_users,backref=db.backref('users', lazy='dynamic'))
#     def __str__(self):
#         return self.email
    
# Create customized model view class
# class MyModelView(sqla.ModelView):

#     def is_accessible(self):
#         if not current_user.is_active or not current_user.is_authenticated:
#             return False

#         if current_user.has_role('superuser'):
#             return True

#         return False

#     def _handle_view(self, name, **kwargs):
#         """
#         Override builtin _handle_view in order to redirect users when a view is not accessible.
#         """
#         if not self.is_accessible():
#             if current_user.is_authenticated:
#                 # permission denied
#                 abort(403)
#             else:
#                 # login
#                 return redirect(url_for('security.login', next=request.url))


#     # can_edit = True
#     edit_modal = True
#     create_modal = True    
#     can_export = True
#     can_view_details = True
#     details_modal = True

# class UserView(MyModelView):
#     column_editable_list = ['email', 'first_name', 'last_name']
#     column_searchable_list = column_editable_list
#     column_exclude_list = ['password']
#     # form_excluded_columns = column_exclude_list
#     column_details_exclude_list = column_exclude_list
#     column_filters = column_editable_list


# class CustomView(BaseView):
#     @expose('/')
#     def index(self):
#         return self.render('admin/custom_index.html')
    # class Item (db.Model):
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
