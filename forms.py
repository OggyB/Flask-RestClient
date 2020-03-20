from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    mail = StringField('userMail', validators=[DataRequired()])
    password = StringField('userPassword', validators=[DataRequired()])