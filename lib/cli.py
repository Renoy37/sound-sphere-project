from helpers import main_menu,add_song,search_song,view_playlists,play_song

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
