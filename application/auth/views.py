from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import UserForm, EditProfileForm
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/auth/login", methods=["GET"])
def view_login_form():
    create_testadmin_if_absent()
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
def view_signup_form():
    form = UserForm()

    return render_template("auth/signup.html", form=form)


@app.route("/auth/users", methods=["POST"])
def create_user():
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


@app.route("/auth/logout", methods=["POST"])
def auth_logout():
    logout_user()
    return redirect(url_for("auth_login"))


@app.route("/auth/users/<user_id>", methods=["GET"])
@login_required
def view_user_page(user_id):

    user = User.get_user_with_statistics(user_id)

    if not user:
        redirect(url_for("topics_index"))

    return render_template("auth/user_page.html", user=user)


@app.route("/auth/users/<user_id>/edit", methods=["GET"])
@login_required
def view_edit_profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        redirect(url_for("topics_index"))
    
    form = EditProfileForm()
    form.description.data = user.description
    
    return render_template("auth/edit_profile.html", form=form)


@app.route("/auth/users/<user_id>/edit", methods=["POST"])
@login_required
def edit_profile(user_id):
    form = EditProfileForm(request.form)

    if not form.validate():
        return render_template("auth/edit_profile.html", form=form)

    user = User.query.filter_by(id=user_id).first()

    if not user:
        redirect(url_for("topics_index"))

    user.description = form.description.data
    db.session().commit()

    return redirect(url_for("view_user_page", user_id=user_id))


def create_testadmin_if_absent():
    testadmin = User.query.filter_by(username="tsohaadmin").first()
    if testadmin:
        return

    pw_hash = bcrypt.generate_password_hash("tsohaadmin").decode("utf-8")

    testadmin = User("tsohaadmin", pw_hash, True)

    db.session().add(testadmin)
    db.session().commit()
