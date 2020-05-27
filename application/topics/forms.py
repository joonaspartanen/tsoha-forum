from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, TextAreaField, SelectMultipleField
from wtforms.validators import ValidationError


class TopicForm(FlaskForm):
    subject = StringField(
        "Subject", [validators.Length(max=100), validators.DataRequired()], render_kw={"placeholder": "Subject"})
    body = TextAreaField("Body", [validators.Length(
        max=1000), validators.DataRequired()], render_kw={"placeholder": "Type your message here"})
    tags = SelectMultipleField('Tags', choices=[], validate_choice=False)

    class Meta:
        csrf = False

    def validate_tags(self, field):
        tag_names = field.data[0].split(",")
        if (len(field.data[0]) == 0):
            raise ValidationError('Please provide at least one tag to describe the topic.')

        for tag_name in tag_names:
            if len(tag_name) > 10:
                raise ValidationError('A tag can be only 10 characters long.')