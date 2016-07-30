import subprocess
from vlc import *
import os
import sys
import time
from read_subtitles import read_subtitles

import speech_recognition as sr
import threading



class speech_thread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        text = speech_query()
        print text

def speech_query():
    r = sr.Recognizer()
    m = sr.Microphone()

    try:
        print("A moment of silence, please...")
        # TO DO: Fix ambient noise?

        #with m as source: r.adjust_for_ambient_noise(source)
        #print("Set minimum energy threshold to {}".format(r.energy_threshold))

        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else: # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))

            return value
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


def play_vlc_video(movie, end_times, dialogues):
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

    triggered = False
    fd = sys.stdin.fileno()

    # To Test
    #end_times[0] = 3000
    i = 0

    # TO DO: Check Thresholds, as well as audio timeout
    while True and not triggered:
        elapsed = player.get_time()
        if elapsed - end_times[i] > 1000:
            i += 1
            continue
        if end_times[i] - elapsed < 2000 and not triggered:
            print "Question at: ", end_times[i], 'is', dialogues[i]
            thread1 = speech_thread(1, "Thread-1", 1)
            thread1.start()

            while thread1.is_alive():
                elapsed = player.get_time()
                if elapsed - end_times[i] > 4000:
                    i += 1
                    break

            print "Resuming"
            triggered = False
            i += 1
            #player.play()
                

if __name__ == '__main__':
    movie = '../dora.mp4'
    subtitles = 'dora.srt'
    read_sub_return = read_subtitles(subtitles)
    end_times = read_sub_return['timestamps']
    dialogues = read_sub_return['dialogues']
    #end_times = [10699]
    play_vlc_video(movie, end_times, dialogues)