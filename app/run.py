#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_cors import CORS
import connexion
import logging
import requests

logging.basicConfig(level=logging.INFO, format='[ %(asctime)s ] %(levelname)s %(message)s')


def healthy_job():
    # 调用同步接口
    requests.get(url='http://127.0.0.1:80/api/status', timeout=30)


if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)
    options = {
        "swagger_ui": True
    }
    app = connexion.FlaskApp(
        __name__,
        specification_dir='specs/',
        options=options
    )
    app.add_api("app_swagger.yaml")

    # Start flask app
    app.run(host='0.0.0.0', port=80, debug=True)
