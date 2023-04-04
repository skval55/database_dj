"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    app.app_context().push()




class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlists_songs'

    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
# playlists_songs = db.Table('playlists_songs',
#                         db.Column('id', db.Integer, primary_key = True, autoincrement= True),
#                         db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id')),
#                         db.Column('song_id', db.Integer, db.ForeignKey('songs.id'))
#                         )



class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    title = db.Column(db.String(50), nullable = False)
    artist = db.Column(db.String)




class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String)

    songs = db.relationship('Song', secondary = 'playlists_songs', backref = 'playlists')
    # ADD THE NECESSARY CODE HERE
