from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField


class MainForm(FlaskForm):

    json = TextAreaField("Json", render_kw={"rows": 10, "cols": 140})
    submit = SubmitField("Submit")
