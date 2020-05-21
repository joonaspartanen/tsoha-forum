from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators


class PostForm(FlaskForm):
    body = TextAreaField("Body", [validators.Length(max=1000), validators.DataRequired(
    )], render_kw={"placeholder": "Type your message here"})

    class Meta:
        csrf = False