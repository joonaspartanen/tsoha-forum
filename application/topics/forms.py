from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, TextAreaField, SelectMultipleField


class TopicForm(FlaskForm):
    subject = StringField(
        "Subject", [validators.Length(max=100), validators.DataRequired()], render_kw={"placeholder": "Subject"})
    body = TextAreaField("Body", [validators.Length(
        max=1000), validators.DataRequired()], render_kw={"placeholder": "Type your message here"})
    tags = SelectMultipleField('Tags', choices=[], validate_choice=False)

    class Meta:
        csrf = False
