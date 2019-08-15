from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_admin.contrib import sqla
import flask_admin
from flask_admin import helpers as admin_helpers
from flask_admin import BaseView, expose

#flask extensions
login_manager = LoginManager()
login_manager.session_protection = 'Strong'
login_manager.login_view = ' auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    admin = flask_admin.Admin(
        app,
        'My Dashboard',
        base_template='my_master.html',
        template_mode='bootstrap3',
    )
    app.config.from_object(config_options[config_name])

    #initalize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # Add model views
    admin.add_view(MyModelView(Role, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Roles"))
    admin.add_view(UserView(User, db.session, menu_icon_type='fa', menu_icon_value='fa-users', name="Users"))
    admin.add_view(CustomView(name="Custom view", endpoint='custom', menu_icon_type='fa', menu_icon_value='fa-connectdevelop',))


    #config uploadset
    configure_uploads(app, photos)

    #Registering bluprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app