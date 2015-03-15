#!/usr/bin/env python
# coding: utf-8
# Copyright © 2015 Wieland Hoffmann
# License: MIT, see LICENSE for details
from flask import abort, Blueprint, redirect, request, render_template, url_for
from json import loads
from mbdata import models
from operator import itemgetter
from sqlalchemy.orm.query import Query
from uuid import UUID
from ..mb_database import db_session
from ..models import db, Playlist

playlist_bp = Blueprint("playlist", __name__)


@playlist_bp.route("/")
def list_playlists():
    playlists = db.session.query(Playlist.data["description"],
                                 Playlist.data["name"],
                                 Playlist.gid)
    return render_template("playlist/list.html", playlists=playlists)


@playlist_bp.route("/<uuid:pid>", methods=["GET"])
def view_playlist(pid):
    playlist = Playlist.query.filter(Playlist.gid == str(pid)).first_or_404()

    recording_ids = [itemgetter("recordingid")(track)
                     for track in playlist.data["tracklist"]]
    recording_query = db_session().query(models.Recording.name,
                                         models.Recording.gid,
                                         models.ArtistCredit.name,
                                         models.Track.gid).\
        join(models.Track).\
        join(models.ArtistCredit).\
        filter(models.Recording.gid.in_(recording_ids))
    recordings = {}
    for name, recordingid, credit, trackid in recording_query.all():
        recordings[recordingid] = (name, credit, trackid)
    return render_template("playlist/single.html",
                           playlist=playlist,
                           recordings=recordings)


@playlist_bp.route("/<uuid:pid>", methods=["POST"])
def add_playlist(pid):
    doc = request.get_data()
    json = loads(doc.encode("utf-8"))

    uuid_from_doc = UUID(json["uuid"])
    if uuid_from_doc != pid:
        abort(400)

    playlist = Playlist.query.filter(Playlist.gid == str(pid)).first()
    if playlist is None:
        playlist = Playlist(gid=str(pid), data=json)
    else:
        playlist.data = json
    db.session.add(playlist)
    db.session.commit()
    return redirect(url_for('playlist.list_playlists'))
