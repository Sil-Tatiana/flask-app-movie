from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

class UserDataForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    rating = SelectField("Rating", validators=[DataRequired()], choices =[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])                                   
    submit = SubmitField('Save Rating')

