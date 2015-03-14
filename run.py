#!/usr/bin/env python
# coding: utf-8
# Copyright © 2015 Wieland Hoffmann
# License: MIT, see LICENSE for details
if __name__ == "__main__":
    from edaboweb.edaboweb import app
    from edaboweb.models import db
    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.run(debug=True)
