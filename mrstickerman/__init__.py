from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mrstickermansecretkey2025'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mrstickerman.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        # Register the blueprints
        from .views import views
        from .admin import admin
        app.register_blueprint(views)
        app.register_blueprint(admin)

    return app