import os

from flask import Flask
app = Flask(__name__, instance_relative_config=True)
import customer.views

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from customer import views

    app.register_blueprint(views.login)

    return app