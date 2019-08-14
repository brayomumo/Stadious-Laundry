from flask import render_template, request,redirect,url_for, abort
from . import main
from flask_login import login_required


# @main.route('/user/uname')
# def profile(uname):
    

@main.route('/')
def index():
    title = "Home"
    return render_template('index.html', title=title)


