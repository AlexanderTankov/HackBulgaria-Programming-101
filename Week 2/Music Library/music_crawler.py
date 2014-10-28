from mutagen.mp3 import MP3
from song import Song
from playlist import Playlist

import os


class MusicCrawler():

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        result = Playlist("Rock'n'roll")
        music_files = [f for f in os.listdir(self.path) if f.endswith('.mp3')]
        for song in music_files:
            audio = MP3(song)
            my_new_song = Song(audio["TIT2"], audio["TPE1"], audio["TALB"], 0, int(audio.info.length), audio.info.bitrate)
            result.add_song(my_new_song)
            print(str(result))
        return result

if __name__ == '__main__':
    crawler = MusicCrawler("/home/alexandar/Documents/Programming-101 Hack BG/Week 2/Music Library")
    playlist = crawler.generate_playlist()
