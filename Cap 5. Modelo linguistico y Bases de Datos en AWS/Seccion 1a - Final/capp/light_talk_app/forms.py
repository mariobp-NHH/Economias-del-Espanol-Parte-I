from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField, StringField
from wtforms.validators import InputRequired

class AddForm(FlaskForm):
  incorrect_sentence = StringField('Frase Incorrecta', [InputRequired()])
  correct_sentence_one = StringField('Frase Correcta 1', [InputRequired()], default="none")
  correct_sentence_two = StringField('Frase Correcta 2', [InputRequired()], default="none")
  correct_sentence_three = StringField('Frase Correcta 3', [InputRequired()], default="none")
  objective = SelectField('Objetivo', [InputRequired()], 
    choices=[('Genero', 'Genero'), ('Número', 'Número')])
  source = SelectField('Fuente', [InputRequired()], 
    choices=[('Inteligencia Artificial', 'Inteligencia Artificial'), ('Persona', 'Persona'), ('Lingüista', 'Lingüista')])
  submit = SubmitField('Añadir')