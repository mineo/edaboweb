#!/usr/bin/env python
# coding: utf-8
# Copyright © 2015 Wieland Hoffmann
# License: MIT, see LICENSE for details
from mbdata import models
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False))


models.Recording.tracks = relationship('Track')


def init_db(engine):
    models.Base.metadata.create_all(bind=engine)
