from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def laman_tidak_ditemukan(error):
    return render_template('404.html'), 404

def create_app(config):
    pass