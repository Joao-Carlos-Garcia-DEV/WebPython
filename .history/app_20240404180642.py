from flask import Flask

def jls_extract_def():
    return "Ola"


app = Flask(jls_extract_def())





@app.route("/")

def ola():

    return "Testando Flask 3"

