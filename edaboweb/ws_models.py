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

pl = {
  "tracklist": [
    {
      "releasetrackid": "1eb2363b-83b1-3527-a845-1164eb3f04ed",
      "recordingid": "4e0b973e-219b-47fb-b3a1-074695e837d6"
    }
  ],
  "name": "test2",
  "timestamp": "2015-01-25T22:01:28.202Z",
  "description": None,
  "uuid": "94b02773-a640-464c-b1cd-7e73908e3728"
}
