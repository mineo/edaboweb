#!/usr/bin/env python
# coding: utf-8
# Copyright © 2016 Wieland Hoffmann
# License: MIT, see LICENSE for details
from schema import Schema, Optional, Or, Use
from uuid import UUID

Track = Schema({"recordingid": Use(UUID),
                Optional("releaseid", default=None): Or(Use(UUID), None),
                Optional("releasetrackid", default=None): Or(Use(UUID), None)})

Playlist = Schema({"name": Use(unicode),
                   "description": Or(None, (Use(unicode))),
                   "timestamp": Use(unicode),
                   "tracklist": [Track],
                   "uuid": Use(UUID)
                   })
