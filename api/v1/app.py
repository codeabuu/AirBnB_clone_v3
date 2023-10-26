#!/usr/bin/python3
"""config file"""

from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)



@app.teardown_appcontext
def teardown_appcont(exception):
    """ends db session"""
    storage.close()


@app.errorhandler(404)
def not_reached(error):
    """Handle non existing pages"""
    e = {
            "error": "Not Found"
            }
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST","0.0.0.0")
    ports = os.getenv("HBNB_API_PORT","5000")
    app.run(host=host, port=ports)
