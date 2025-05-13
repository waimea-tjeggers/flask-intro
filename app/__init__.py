from flask import Flask
from flask import render_template
from random import randint

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("pages/home.jinja")


@app.get("/test/")
def test():
    return render_template("pages/test.jinja")

@app.get("/about/")
def about():
    return render_template("pages/about.jinja")

@app.get("/random/")
def random():
    randNum = randint(1,1000)
    return render_template("pages/random.jinja", Number=randNum)

@app.errorhandler(404)
def notFound(error):
    return render_template ("pages/404.jinja")

