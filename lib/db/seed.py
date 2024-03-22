from models import Playlist, Song, User, Base
from faker import Faker
import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

fake = Faker()

# Establishing a connection to the database which is in the lib directory
db_path = '../soundsphere.db'

# engine = create_engine('sqlite:///soundsphere.db')
engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':

    # populating the user table
    for i in range(70):
        # creating names for the songs to test the names table
        user = User(username=fake.name())
        session.add(user)
    session.commit()

    print("artists seeded in the database")

    # populating the song table
    for i in range(70):
        song = Song(
            title=fake.word(),
            artist=fake.name(),
            duration=random.randint(120, 600)
        )
        session.add(song)
    session.commit()

    # print("songs seeded in the database")

    # populating the playlist table
    users = session.query(User).all()

    for i in range(70):
        playlist = Playlist(
            name=fake.sentence(nb_words=3),
            # associating random user with the playlist
            user=random.choice(users)
        )
        session.add(playlist)

    session.commit()
    print("Playlist seeded in the database")
