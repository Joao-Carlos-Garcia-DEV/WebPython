" Teste Flask "

from flask import Flask

app = Flask("Ola")

@app.route("/")
def ola():
    "Teste 
    return "Testando Flask 3"
