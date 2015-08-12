from mutagen.mp3 import MP3
import pygame
from song import Song
from playlist import Playlist

import os


class MusicCrawler():

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        result = Playlist("Rock'n'roll")
        music_files = [f for f in os.listdir(self.path) if f.endswith('.mp3') or f.endswith('.MP3')]
        for song in music_files:
            audio = MP3(self.path + "/" + song)
            print(audio)
            my_new_song = Song(audio["TIT2"], audio["TPE1"], audio["TALB"], 0, int(audio.info.length), audio.info.bitrate)
            result.add_song(my_new_song)
        return result


def start_song_with_num(array_of_songs, num):
    if num <= len(array_of_songs):
        pygame.mixer.init()
        pygame.mixer.music.load(array_of_songs[num - 1])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            temp_imput = input()
            if temp_imput.lower() == "stop":
                pygame.mixer.music.stop()
                return True
            elif temp_imput.lower() == "exit":
                pygame.mixer.music.stop()
                return False
    else:
        print("Dont have song with that number")
        return True


def start_playlist(array_of_songs):
    temp_flag = True
    while temp_flag:
        for elem in array_of_songs:
            pygame.mixer.init()
            pygame.mixer.music.load(elem)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                    temp_imput = input("chose command:\nnext - for next song, stop - for stop music or exit\n")
                    if temp_imput.lower() == "next":
                        break
                    elif temp_imput.lower() == "stop":
                        pygame.mixer.music.stop()
                        return True
                    elif temp_imput.lower() == "exit":
                        pygame.mixer.music.stop()
                        return False
                    else:
                        print("This command is not valid")
                    pygame.mixer.music.stop()

if __name__ == '__main__':
    crawler = MusicCrawler("/home/alexandar/Documents/Programming-101/Week2/Music Library")
    playlist = crawler.generate_playlist()
    songs_arr = []
    for elem in playlist.songs:
        print(elem.artist, elem.title)
        songs_arr.append("{} - {}.mp3".format(elem.artist, elem.title))

    print("Playlist:")
    for idx, elem in enumerate(songs_arr):
        print("[{}] {}".format(idx + 1, elem))
    global_flag = True
    while global_flag:
        temp_flag = True
        while temp_flag:
            input_str = input("chose command:\nplay all songs,number of the song that you want to hear or exit\n")
            if input_str.lower() == "play all songs":
                if not start_playlist(songs_arr):
                    temp_flag = False
                    global_flag = False
            elif input_str.lower() == "exit":
                temp_flag = False
                global_flag = False
            elif not input_str.isdigit():
                print("This command is not valid")
                temp_flag = False
            elif start_song_with_num(songs_arr, int(input_str)):
                temp_flag = False
            else:
                temp_flag = False
                global_flag = False
