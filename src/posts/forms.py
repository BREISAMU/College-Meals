from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

type_choices = [('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Dessert', 'Dessert')]
price_choices = [('Cheap', 'Cheap'), ('Moderately priced', 'Moderately priced'), ('Expensive', 'Expensive')]


class PostForm(FlaskForm):
    title = StringField('Meal Title', validators=[DataRequired()])
    type = SelectField(u'Type of meal?', choices=type_choices)
    price = SelectField(u'Price range of meal?', choices=price_choices)
    content = TextAreaField('Recipe (Ingredients, Measurements, Procedure, etc.)', validators=[DataRequired()])
    submit = SubmitField('Post')

