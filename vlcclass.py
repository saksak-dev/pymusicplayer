import os
import vlc





class player:

    def __init__(self):
        self.volume = 80
        self.vlc_instance = vlc.Instance()
        self.vlc_player = self.vlc_instance.media_player_new()
        self.is_playing = True
        self.songs = []
        self. song_index = 0


    def list_songs(directory):
        song_list=[]
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
        self.volume = min(self.volume + 10, 100)
        self.vlc_player.audio_set_volume(self.volume)
        print(f"Volume set to {self.volume}")



