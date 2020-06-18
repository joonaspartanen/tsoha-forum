from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import ValidationError


class TopicForm(FlaskForm):
    subject = StringField(
        "Subject", [validators.Length(max=100), validators.DataRequired()], render_kw={"placeholder": "Subject"})
    body = TextAreaField("Message body", [validators.Length(
        max=1000), validators.DataRequired()], render_kw={"placeholder": "Type your message here"})
    tags = SelectMultipleField("Tags", choices=[], validate_choice=False)

    def validate_tags(self, field):
        tag_names = field.data[0].split(",")
        if (len(field.data[0]) == 0):
            raise ValidationError(
                "Please provide at least one tag to describe the topic.")

        for tag_name in tag_names:
            if len(tag_name) > 20:
                raise ValidationError("A tag can be only 20 characters long.")


class SearchForm(FlaskForm):
    subject = StringField("Subject contains", [validators.Length(
        max=100)], render_kw={"placeholder": "Subject"})
    author = StringField("Author name contains", [validators.Length(
        max=100)], render_kw={"placeholder": "Author"})
