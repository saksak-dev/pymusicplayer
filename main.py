import vlcclass
import time
import os
from pynput import keyboard
import vlc


musicplayer = vlcclass.Player()

#TODO switch to curses
def on_press(key):
    try:
        if key == keyboard.Key.left:
            print()
            musicplayer.previous_song()
            print()  # Move to a new line after handling the key press
        elif key == keyboard.Key.right:
            print()
            musicplayer.next_song()
            print()  # Move to a new line after handling the key press
        elif key == keyboard.Key.up:
            print()
            musicplayer.increase_volume()
            print()  # Move to a new line after handling the key press
        elif key == keyboard.Key.down:
            print()
            musicplayer.decrease_volume()
            print()  # Move to a new line after handling the key press
        elif key.char == 'p':
            print()
            musicplayer.toggle_play()
            print()  # Move to a new line after handling the key press
        elif key.char == 'd':
            print()
            print("Select a song to delete:")
            for index, song in enumerate(musicplayer.songs):
                print(f"\033[1m{index + 1}\033[0m {song} ")
            song_number = input("Please enter the song number to delete:\n")
            musicplayer.del_song(song_number)
            print()
    except AttributeError:
        # Handle special keys
        pass


def main():
    global musicplayer
    musicplayer.songs = musicplayer.list_songs("/home/ognjen/Music")
    if not musicplayer.songs:
        print("No audio files found")

    print("Available songs:")
    for i, song in enumerate(musicplayer.songs):
        print(f"{i + 1}: {song}")

    musicplayer.play_song(musicplayer.songs[musicplayer.song_index])

    with keyboard.Listener(on_press=on_press) as listener:
        print("Press the left/right arrow keys to navigate songs, and up/down arrow keys to adjust volume.")
        print("Press 'p' to pause or continue the current track.")
        # Keep the script running and listening for key presses
        while True:
            if musicplayer.vlc_player.get_state() == vlc.State.Ended:
                musicplayer.next_song()
            time.sleep(1)


if __name__ == "__main__":
    main()

