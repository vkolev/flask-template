from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import LoginForm
from models import User
import hashlib
from datetime import datetime


@app.before_request
def before_request():
    g.user = current_user


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(page=1):
    return render_template("index.html",
                           title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        q = User.query.filter_by(username=form.username.data,
                                 password=hashlib.sha1(form.password.data).hexdigest()).first()
        if q is not None:
            g.user = q
            login_user(q)
            flash("Logged in successfully.")
            return redirect('/index')
    return render_template("login.html",
                           title="Sign In",
                           form=form)


@app.route('/admin')
@login_required
def admin():
    g.user = current_user
    return render_template("admin.html",
                           title="Administration",
                           user=g.user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
