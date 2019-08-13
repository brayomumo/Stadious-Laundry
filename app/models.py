from . import create_app,db
from flask_security import Security,SQLAlchemyUserDatastore, UserMixin,RoleMixin,login_required,current_user
from werkzeug.security import generate_password_hash,check_password_hash



# Define models
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)
