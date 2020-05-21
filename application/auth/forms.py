from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class UserForm(FlaskForm):
    username = StringField("Username", [validators.Length(
        min=5)], render_kw={"placeholder": "Username"})
    password = PasswordField("Password", [validators.Length(min=8)], render_kw={"placeholder": "Password"})

    class Meta:
        csrf = False
