#!/usr/bin/env python
# coding: utf-8
# Copyright © 2015 Wieland Hoffmann
# License: MIT, see LICENSE for details
from flask import abort, Blueprint, render_template

playlist_bp = Blueprint("playlist", __name__)


@playlist_bp.route("/")
def list_playlists():
    return render_template("playlist/list.html")
