from flask import Flask

application = Flask(__name__)



from capp.home.routes import home
from capp.business.routes import business
from capp.light_talk_app.routes import light_talk_app


application.register_blueprint(home)
application.register_blueprint(business)
application.register_blueprint(light_talk_app)


