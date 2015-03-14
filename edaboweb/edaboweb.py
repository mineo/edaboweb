#!/usr/bin/env python
# coding: utf-8
# Copyright © 2015 Wieland Hoffmann
# License: MIT, see LICENSE for details
from flask import Flask

from .blueprints.index import index_bp
from .blueprints.playlist import playlist_bp
from .models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://edaboweb@localhost/edaboweb"
app.register_blueprint(index_bp)
app.register_blueprint(playlist_bp, url_prefix="/playlist")
db.init_app(app)
