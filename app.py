appVersion = "v0.0.1"
senseBoxes = "615a7b227ea3fe001c7daa7e", "6132aaf6d5bb40001c370189", "6184b16751eeff001ba45c98"

from flask import Flask
from temperature import *

app = Flask(__name__)

@app.route("/")
def version():
    return appVersion

@app.route('/temperature')
def temperature():
    return "{:.2f}".format(avgTemperature(senseBoxes))
