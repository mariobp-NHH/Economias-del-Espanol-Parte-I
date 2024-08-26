from flask import render_template, Blueprint, redirect, url_for
from capp.models import Sentence
from capp.light_talk_app.forms import AddForm
from flask_login import login_required, current_user
from capp import db

light_talk_app=Blueprint('light_talk_app',__name__)

@light_talk_app.route('/light_talk_app')
def light_talk_app_home():
    return render_template('/light_talk_app/light_talk_app.html', title='light_talk_app')

#Add a new sentence
@light_talk_app.route('/light_talk_app/añadir_frase', methods=['GET','POST'])
@login_required
def add_sentence():
    form = AddForm()
    if form.validate_on_submit():
        incorrect_sentence = form.incorrect_sentence.data
        correct_sentence_one = form.correct_sentence_one.data
        correct_sentence_two = form.correct_sentence_two.data
        correct_sentence_three = form.correct_sentence_three.data
        your_sentence = "none"
        objective = form.objective.data
        source = form.source.data
        result_string = "none"
        result_num= "nan"
        group = 'general'
        university = 'University of Salamanca'
        year = 2024
 
        sentence = Sentence(incorrect_sentence=incorrect_sentence, correct_sentence_one=correct_sentence_one, correct_sentence_two=correct_sentence_two, correct_sentence_three=correct_sentence_three, correct_sentence_four="none", your_sentence=your_sentence, objective=objective, source=source, result_string=result_string, result_num=result_num,  group=group, university=university, year=year, author=current_user)
        db.session.add(sentence)
        db.session.commit()
        return redirect(url_for('light_talk_app.light_talk_app_home'))
    return render_template('light_talk_app/add_sentence.html', title='add sentence', form=form)
    