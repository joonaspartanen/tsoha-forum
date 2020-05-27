from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import UserForm
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/auth/login", methods=["GET"])
def auth_login_form():    
    return render_template("auth/login.html", form=UserForm())


@app.route("/auth/login", methods=["POST"])
def auth_login():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/login.html", form=form)

    user = User.query.filter_by(
        username=form.username.data).first()

    if not user:
        return render_template("auth/login.html", form=form, error="Incorrect username")

    if not bcrypt.check_password_hash(user.pw_hash, form.password.data):
        return render_template("auth/login.html", form=form, error="Incorrect password")

    login_user(user)

    return redirect(url_for("index"))


@app.route("/auth/signup", methods=["GET"])
def auth_signup_form():
    form = UserForm()

    return render_template("auth/signup.html", form=form)


@app.route("/auth/users", methods=["POST"])
def auth_create():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/signup.html", form=form)

    username = form.username.data
    user = User.query.filter_by(username=username).first()

    if user:
        return render_template("auth/signup.html", form=form, error="Username " + username + " is already taken. Please select another username.")

    pw_hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

    new_user = User(username, pw_hash, False)

    db.session().add(new_user)
    db.session().commit()

    return redirect(url_for("auth_login"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("auth_login"))

