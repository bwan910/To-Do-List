from pygame import mixer
import random
import calendar


_songs = ['C:/Users/SpectreX/Desktop/To-Do List/Work.mp3',
          'C:/Users/SpectreX/Desktop/To-Do List/Make.mp3',
          'C:/Users/SpectreX/Desktop/To-Do List/Mean.mp3',
          'C:/Users/SpectreX/Desktop/To-Do List/See.mp3']

# Function to play music


def play_music():
    next_song = random.choice(_songs)
    mixer.init()
    mixer.music.load(next_song)
    mixer.music.play()

# Function to stop music


def stop_music():
    mixer.music.stop()
