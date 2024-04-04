from flask import Flask

app = Flask('Ola')


@app.route("/")
def ola():
    return "Testando Flask 3"
