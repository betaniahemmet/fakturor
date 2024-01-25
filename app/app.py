from flask import Flask, flash, request, render_template, url_for, redirect
from waitress import serve

from .file_functions import create_invoices, magnus_order
from .routes import main_blueprint
from .config import secret

def create_app():
    app = Flask(__name__)
    app.secret_key = secret

    # Register the main blueprint
    app.register_blueprint(main_blueprint)

    return app

