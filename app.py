"""
A basic flask application which uses opensensemap.org data
"""

from flask import Flask
from temperature import avg_temperature

# pylint: disable=C0103
appVersion = "v0.0.1"
senseBoxes = "615a7b227ea3fe001c7daa7e", "6132aaf6d5bb40001c370189", "6184b16751eeff001ba45c98"

app = Flask(__name__)

@app.route("/")
def version():
    """shows app version"""
    return appVersion

@app.route('/temperature')
def temperature():
    """shows avg temperature of all locations passed as arguments"""
    return f"{avg_temperature(senseBoxes):.2f}"
