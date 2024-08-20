from flask import Flask
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
  return "<h1>Home</h1> <br> <p>En este proyecto vamos a desarrollar ...</p>"

@application.route('/business')
def business():
    return "<h1>Modelo de negocio</h1> <br><br> <p>Nuestro modelo de negocio se basa en ...</p>"

@application.route('/light_talk_app')
def light_talk_app():
    return "<p>Light-Talk App ...</p>"

if __name__=='__main__':
  application.run(debug=True)  