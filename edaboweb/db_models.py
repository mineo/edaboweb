#!/usr/bin/env python
# coding: utf-8
# Copyright © 2015 Wieland Hoffmann
# License: MIT, see LICENSE for details
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB, UUID

db = SQLAlchemy()


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(UUID, nullable=False)
    data = db.Column(JSONB, nullable=False)
