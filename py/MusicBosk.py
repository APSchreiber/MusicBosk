# MusicBosk
# MusicBosk.py

# Author: Andrew Schreiber
# Created: 11/10/18
# Modified: 11/10/18

'''
A Python music box
'''

print "Loading..."
import os, sys, traceback, datetime, collections, random, winsound
from time import sleep 

#####################################################################

note_freqs = {
    "C": 16.351,
    "D": 18.354,
    "E": 20.601,
    "F": 21.827,
    "G": 24.499,
    "A": 27.5,
    "B": 30.868
    }

note_durs = {
    "whole": 1,
    "half": 0.5,
    "quarter": 0.25,
    "eighth": 0.125,
    "sixteenth": 0.0625
    }

scales = {
    "major": [2, 2, 1, 2, 2, 2, 1],
    "minor": [2, 1, 2, 2, 1, 2, 2]
    }

#####################################################################

# return an ordered dict
def order_dict(dictionary, ordering):
    # order by key
    if ordering == "key":
        return collections.OrderedDict(sorted(dictionary.items(), key=lambda t: t[0]))
    # order by value
    elif ordering == "value":
        return collections.OrderedDict(sorted(dictionary.items(), key=lambda t: t[1]))
    # no order
    else:
        return dictionary

# play a note
def play_note(note, rhythm, octave):

    # get the octave multiplier
    multiplier = 1
    if octave > 0:
        if octave == 1:
            multiplier = 2
        else:
            multiplier = 2 ** octave

    # get the duration
    duration = int(note_durs[rhythm] * 1000)

    # generate the tone
    tone = int(note_freqs[note] * multiplier)
    winsound.Beep(tone, duration)
            

#####################################################################

try:

    # play a c major scale
    scale = ["C", "D", "E", "F", "G", "A", "B"]
    octave = 5
    for note in scale:
        play_note(note, "half", octave)
    play_note(scale[0], "half", octave + 1)
    

    
    
except:

    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]

    print "\nError: " + tbinfo
    
