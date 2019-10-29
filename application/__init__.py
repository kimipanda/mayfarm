from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from application.main import main_blueprint

# Configure
app = Flask(__name__)

if app.config['ENV'] == 'production':
    app.config.from_object('application.config.config.ProductionConfig')
else:
    app.config.from_object('application.config.config.DevelopmentConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(main_blueprint)
