from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Song, Base, Playlist, User

# Establishing a connection to the database which is in the lib directory
db_path = '../lib/soundsphere.db'

engine = create_engine(f'sqlite:///{db_path}')
# engine = create_engine('sqlite:///soundsphere.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def main_menu():
    print("Main Menu")
    print("1. Add Song")
    print("2. Search Song")
    print("3. View Playlists")
    print("4. Play Song")
    print("5. Exit")


def add_song():
    print("Add Song")

    # taking the title,artist and duration to add a song t the database
    title = input("Enter song title: ")
    artist = input("Enter artist of the song: ")
    duration_minutes = int(input("Enter duration of the song in minutes: "))
    duration_seconds = int(input("Enter duration of the song in seconds: "))

    total_duration_seconds = (duration_minutes * 60) + duration_seconds

    # adding and committing the new song to the database
    song = Song(title=title, artist=artist, duration=total_duration_seconds)
    session.add(song)
    session.commit()

    print("Song added successfully!")


def search_song():
    print("Search Song")
    print("1. Search by Title")
    print("2. Search by Artist")
    # print("3. Back to Main Menu")

    search_choice = input("Enter Choice: ")

    # if statement to handle searching songs by title and artist name and using ilike to prevent case sensitivity errors
    if search_choice == "1":
        title = input("Enter the title of the song: ")
        songs = session.query(Song).filter(
            Song.title.ilike(f"%{title}%")).all()
        display_song(songs)
    elif search_choice == "2":
        artist = input("Enter the artist: ")
        songs = session.query(Song).filter(
            Song.artist.ilike(f"%{artist}%")).all()
        display_song(songs)
    # elif search_choice == "3":
    #     return
    else:
        print("Invalid Choice")

# function to display the songs after searching


def display_song(songs):
    if not songs:
        print("No matching songs found. ")
    else:
        print("Matching Songs: ")
        for song in songs:
            duration_minutes, duration_seconds = duration_format(
                song.duration)
            print(
                f"Title: {song.title}, Artist: {song.artist}, Duration:{duration_minutes}minutes {duration_seconds} seconds")


def view_playlists(user_id):
    print("View PLaylists")
    # searching a playlist associated by a certain user
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print("Use not found")
        return

    playlists = user.playlists

    # if to show the playlist of the user
    if not playlists:
        print("No playlists found for this user ")
    else:
        print("Playlists: ")
        for playlist in playlists:
            print(f"Playlist Name: {playlist.name}")
            print("Songs")
            for song in playlist.songs:
                duration_minutes, duration_seconds = duration_format(
                    song.duration)
                print(
                    f"Title: {song.title}, Artist: {song.artist}, Duration:{duration_minutes}minutes {duration_seconds} seconds")


def play_song():
    print("Paying Songs")
    title = input("Enter the title of the song you want to play: ")

    song = session.query(Song).filter_by(title=title).first()

    if song:
        duration_minutes, duration_seconds = duration_format(song.duration)
        print(
            f"Title: {song.title}, Artist: {song.artist}, Duration:{duration_minutes}minutes {duration_seconds} seconds")
    else:
        print("song not found.")


# function to display the time in minutes and seconds since it is stored in the database in seconds
def duration_format(duration):
    # getting the songs minutes
    duration_minutes = duration // 60
    # getting the songs seconds
    duration_seconds = duration % 60
    return duration_minutes, duration_seconds


def cli():
    # you can change the user id to see different user's playlists
    user_id = 17
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_song()
            break
        elif choice == "2":
            search_song()
            break
        elif choice == "3":
            view_playlists(user_id)
            break
        elif choice == "4":
            play_song()
            break
        elif choice == "5":
            print("Exiting....")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    cli()
