" Teste Flask "

from flask import Flask

app = Flask("Ola")

@app.route("/")
def ola():
    "Teste Flask"
    return "Testando Flask 4"
