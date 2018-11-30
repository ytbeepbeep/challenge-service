from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from challengeservice.database import db
from challengeservice.views import blueprints


def create_app():
    app = Flask(__name__)

    app.config['WTF_CSRF_SECRET_KEY'] = 'A SECRET KEY'
    app.config['SECRET_KEY'] = 'ANOTHER ONE'

    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///challenges.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
        blueprint.app = app

    # Init database
    db.init_app(app)
    db.create_all(app=app)
    return app


def main():  # pragma: no cover
    app = create_app()
    app.run(host="0.0.0.0",port=5005,debug=True)


if __name__ == '__main__':
    main()
