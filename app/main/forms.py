from flask_wtf import FlaskForm
from wtforms import TextAreaField,SelectField,SubmitField,
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = TextAreaField('pitch',validators=[Required()])
    my_category = SelectField('category',desired=[('interview','interview'),('product','product'),('job','job'),('pick-up-line','pick-up-line')], validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('comment on your desired pitch', validators=[Required()])
    submit = SubmitField('Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators=[Required()])
    submit = SubmitField('Submit')
