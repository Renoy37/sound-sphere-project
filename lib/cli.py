from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Song, Base

# Establishing a connection to the database
db_path = './db/soundsphere.db'

engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def main_menu():
    print("Main Menu")
    print("1. Add Song")
    print("2. Search Song")
    print("3. View Playlists")
    print("4. Playing Songs")
    print("5. Exit")


def add_song():
    print("Add Song")

    title = input("Enter song title: ")
    artist = input("Enter artist of the song: ")
    duration = int(input("Enter duration of the song: "))

    song = Song(title=title, artist=artist, duration=duration)
    session.add(song)
    session.commit()

    print("Song added successfully!")


def cli():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_song()
            break
        elif choice == "2":
            pass
            break
        elif choice == "3":
            pass
            break
        elif choice == "4":
            pass
            break
        elif choice == "5":
            print("Exiting....")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    cli()
