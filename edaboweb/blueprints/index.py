#!/usr/bin/env python
# coding: utf-8
# Copyright © 2015 Wieland Hoffmann
# License: MIT, see LICENSE for details
from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html')
