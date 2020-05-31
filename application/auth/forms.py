from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, validators


class UserForm(FlaskForm):
    username = StringField("Username", [validators.Length(
        min=5), validators.DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField("Password", [validators.Length(min=8), validators.DataRequired()], render_kw={
                             "placeholder": "Password"})

    class Meta:
        csrf = False


class EditProfileForm(FlaskForm):
    description = TextAreaField("Description", [validators.Length(
        max=1000), validators.DataRequired()], render_kw={"placeholder": "Describe yourself"})

    class Meta:
        csrf = False
