import os
import vlc


class player:

    def __init__(self):
        self.volume = 80
        self.vlc_instance = vlc.Instance()
        self.vlc_player = self.vlc_instance.media_player_new()
        self.is_playing = False
        self.songs = []
        self.song_index = 0

    def list_songs(directory):
        song_list = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.mp3', '.wav', '.flac')):
                    song_list.append(os.path.join(root, file))
        return song_list

    def play_song(self, song):
        """Play the song"""
        media = self.vlc_instance.media_new(song)
        self.vlc_player.set_media(media)
        self.vlc_player.play()
        self.is_playing = True
        song_name = os.path.splitext(os.path.basename(song))[0]
        print(f"Playing {song_name}")

    def next_song(self):
        self.song_index = self.song_index + 1
        self.play_song(self.songs[self.song_index])

    def previous_song(self):
        self.song_index = self.song_index - 1
        self.play_song(self.songs[self.song_index])

    def increase_volume(self):
        self.volume = min(self.volume + 5, 100)
        self.vlc_player.audio_set_volume(self.volume)
        print(f"Volume set to {self.volume}")

    def decrease_volume(self):
        self.volume = max(self.volume - 5, 0)
        self.vlc_player.audio_set_volume(self.volume)
        print(f"Volume set to {self.volume}")

    def toggle_play(self):
        if self.is_playing:
            self.vlc_player.pause()
        else:
            self.vlc_player.play()
        self.is_playing = not self.is_playing
        current = "playing" if self.is_playing else "paused"
        print(f"Track is now {current}")

    def del_song(self, song_number):
        """deletes song by number"""
        try:
            if 0 <= int(song_number) - 1 < len(self.songs):
                del self.songs[int(song_number) - 1]
                print("Song deleted")
            else:
                print("Invalid song number")
        except ValueError:
            print("Invalid input")

        for index, song in enumerate(self.songs):
            print(f"\033[1m{index + 1}\033[0m {song} ")
