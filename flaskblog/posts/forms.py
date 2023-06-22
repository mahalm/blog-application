from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm): # takes in information for post
    title = StringField('Title', validators=[DataRequired()]) # validator, must enter data
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post') 
    