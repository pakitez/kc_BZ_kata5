from flask import Flask

app = Flask(__name__)

@app.route("/")#decorador que hace referencia a la funcion posterior
def hello_world():# el nombre de la funcion de igual
    return "<p>Hola, mundo!</p>"

@app.route('/bye')
def ciao():
    return "<p>Ciao!</p>"
