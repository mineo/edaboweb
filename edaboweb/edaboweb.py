#!/usr/bin/env python
# coding: utf-8
# Copyright © 2015 Wieland Hoffmann
# License: MIT, see LICENSE for details
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.uuid import FlaskUUID
from sqlalchemy import create_engine

from .blueprints.index import index_bp
from .blueprints.playlist import playlist_bp
from .models import db
from .mb_database import db_session

app = Flask(__name__)
Bootstrap(app)
FlaskUUID(app)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "postgresql://edaboweb@localhost/edaboweb"
app.config["MUSICBRAINZ_DATABASE_URI"] = \
    "postgresql://musicbrainz@localhost/musicbrainz"

engine = create_engine(app.config["MUSICBRAINZ_DATABASE_URI"],
                       convert_unicode=True)
db_session.configure(bind=engine)

app.register_blueprint(index_bp)
app.register_blueprint(playlist_bp, url_prefix="/playlist")
db.init_app(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
