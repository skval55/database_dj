from app import db
from models import Playlist, Song, PlaylistSong

db.drop_all()
db.create_all()

pl = Playlist(name="Go Hard", description='go hard in the paint with these songs')
db.session.add(pl)
db.session.commit()
song = Song(title="rocksong", artist='rock artist')
db.session.add(song)
db.session.commit()
pls = PlaylistSong(playlist_id= 1, song_id=1)
db.session.add(pls)
db.session.commit()
