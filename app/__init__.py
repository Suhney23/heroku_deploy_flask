"""A simple flask web app"""
import os
from flask import Flask


def page_not_found(e):
    return render_template("404.html"), 404


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'

    app.register_error_handler(404, page_not_found)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app
