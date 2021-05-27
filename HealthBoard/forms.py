from wtforms import Form
from wtforms.fields import IntegerField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, InputRequired, ValidationError


class InputData(Form):

    height = IntegerField('height', validators=[DataRequired()])
    weight = IntegerField('weight', validators=[DataRequired(), InputRequired()])
    age = IntegerField('age',validators=[DataRequired(), InputRequired()])
    waist = IntegerField('waist', validators=[DataRequired(), InputRequired()])
    gender = RadioField('man', choices=['Man','Woman'])

    

