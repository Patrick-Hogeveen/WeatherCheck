import os

from flask import Flask


def create_app(test_config=None):
    # create app
    app = Flask(__name__, instance_relative_config=True)
    
    # add config params
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

    from . import db
    db.init_app(app)

    from . import weather
    app.register_blueprint(weather.bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # default page
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app