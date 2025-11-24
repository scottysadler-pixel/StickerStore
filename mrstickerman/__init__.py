from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mrstickermansecretkey2025'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mrstickerman.sqlite'
    db.init_app(app)

    # Register the blueprints
    from .views import views
    from .admin import admin
    app.register_blueprint(views)
    app.register_blueprint(admin)

    return app