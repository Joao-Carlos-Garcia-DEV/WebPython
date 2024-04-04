from flask import Flask

app = Flask("Ola")

@app.route("/")
def ola():
    """Function printing python version."""
    return "Testando Flask 3"
