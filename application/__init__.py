from flask import Flask, render_template
from application.config.config import Config

#Configure
app = Flask(__name__)
app.config.from_object(Config)

from application.main import main_blueprint
app.register_blueprint(main_blueprint)

"""
persons = [
    {'name': 'may1', 'count': 30},
    {'name': 'may2', 'count': 10},
    {'name': 'may3', 'count': 60},
]   
@app.route('/')
def index():
    return render_template('index.html', persons=persons)
"""