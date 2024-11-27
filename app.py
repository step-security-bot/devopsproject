"""
A basic flask application which uses opensensemap.org data
"""

from flask import Flask, jsonify
from temperature import avg_temperature

APP_VERSION = "v0.0.1"
senseboxes = "615a7b227ea3fe001c7daa7e", "6132aaf6d5bb40001c370189", "6184b16751eeff001ba45c98"

app = Flask(__name__)

@app.route("/")
def version():
    """shows app version"""
    return jsonify(version = APP_VERSION)

@app.route('/temperature')
def temperature():
    """shows avg temperature of all locations passed as arguments"""
    return jsonify(avg_temperature = f"{avg_temperature(senseboxes):.2f}")
