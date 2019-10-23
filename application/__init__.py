from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from application.config.config import Config
from application.main import main_blueprint

# Configure
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

app.register_blueprint(main_blueprint)
