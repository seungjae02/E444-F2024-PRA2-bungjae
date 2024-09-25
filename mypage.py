from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class MyForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is UofT Email address?', validators=[DataRequired(), Email(),
                                                    Regexp('.*utoronto.*', 0,
                                                    'You must enter a UofT Email!')])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')

        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))

    current_time=datetime.utcnow()
    return render_template('user.html', current_time=current_time, form=form, name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

# if __name__ == '__main__':
#     app.run()