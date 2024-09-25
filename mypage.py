from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    current_time=datetime.utcnow()
    return render_template('user.html', current_time=current_time)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

# if __name__ == '__main__':
#     app.run()