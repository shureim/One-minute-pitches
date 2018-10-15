from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    my_category = SelectField('Category',
                              choices=[('Interview-Pitch', 'Interview Pitch'), ('Product-Pitch', 'Product Pitch'),
                                       ('Promotion-Pitch', 'Promotion Pitch'), ('Business', 'Business'), ('pick-up-lines', 'pick-up-lines')], validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write something about yourself', validators=[Required()])
    submit = SubmitField('Submit')


