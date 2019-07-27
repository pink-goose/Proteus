from flask import Flask
from extensions import (
    init_cors,
)
from skills import Skill


def create_app():
    app = Flask(__name__)
    init_extensions(app)
    init_blueprints(app)
    run_proteus(app)
    return app


def init_extensions(app):
    init_cors(app)
    return


def init_blueprints(app):
    from api.routes import api_bp
    app.register_blueprint(api_bp)
    return


# experimental
# rename to init_proteus and add other inits
def run_proteus(app):
    app.skill_inits = Skill()
    print('Proteus runned')
    return


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', threaded=True)
