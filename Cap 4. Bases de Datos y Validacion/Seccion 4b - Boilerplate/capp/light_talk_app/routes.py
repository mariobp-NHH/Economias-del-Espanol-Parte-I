from flask import render_template, Blueprint
from capp.light_talk_app.forms import AddForm
from capp.models import Sentence

light_talk_app=Blueprint('light_talk_app',__name__)

@light_talk_app.route('/light_talk_app')
def light_talk_app_home():
    return render_template('/light_talk_app/light_talk_app.html', title='light_talk_app')

#Add a new sentence
@light_talk_app.route('/light_talk_app/añadir_frase', methods=['GET','POST'])
def add_sentence():
    form = AddForm()
    return render_template('light_talk_app/add_sentence.html', title='add sentence', form=form)
    