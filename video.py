import subprocess
from vlc import *
import ctypes
from ctypes.util import find_library
import os
import sys
import functools
import time
from read_subtitles import read_subtitles


def play_vlc_video(movie):
    try:
        from msvcrt import getch
    except ImportError:
        import termios
        import tty

        def getch():  # getchar(), getc(stdin)  #PYCHOK flake
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            return ch

    # Need --sub-source=marq in order to use marquee below
    instance = Instance(["--sub-source=marq"] + sys.argv[1:])

    media = instance.media_new(movie)

    player = instance.media_player_new()
    player.set_media(media)
    player.play()


    def quit_app():
        """Stop and exit"""
        sys.exit(0)


    keybindings = {
        ' ': player.pause,
        'q': quit_app,
        }

    while True:
        k = getch()

        if k in keybindings:
            keybindings[k]()


if __name__ == '__main__':
    movie = '../dora.mp4'
    subtitles = 'dora.srt'
    end_times = read_subtitles(subtitles)
    print end_times
    player = play_vlc_video(movie)