#!/usr/bin/env python
# coding: utf-8
# Copyright © 2015, 2016 Wieland Hoffmann
# License: MIT, see LICENSE for details
if __name__ == "__main__":
    from edaboweb.edaboweb import app, engine
    from edaboweb.mb_database import init_db
    from edaboweb.db_models import db
    init_db(engine)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.run(debug=True)
