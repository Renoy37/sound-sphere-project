from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# establishing many to many relationships for the playlists and songs table
playlist_song_intermediary = Table(
    'playlist_song_intermediary',
    Base.metadata,
    Column('playlist_id', Integer, ForeignKey('playlist.id')),
    Column('song_id', Integer, ForeignKey('song.id'))
)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(), unique=True, nullable=False)
    # establishing one to may relationship between users and playlists
    playlists = relationship("Playlist", back_populates="user")


class Playlist(Base):
    __tablename__ = 'playlist'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="playlists")
    songs = relationship(
        "Song", secondary=playlist_song_intermediary, back_populates="playlists")


class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    artist = Column(String())
    duration = Column(Integer())
    playlists = relationship(
        "Playlist", secondary=playlist_song_intermediary, back_populates="songs")
