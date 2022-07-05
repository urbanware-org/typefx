#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# TypeFX - Typewriter effect text printer
# Experimental keystroke sound module
# Copyright (C) 2022 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/typefx
# GitLab: https://gitlab.com/urbanware-org/typefx
#

__version__ = "1.1.4"   # with keystroke sound effects

#
# As already mentioned above, this is an experimental version of the TypeFX
# module, which, unlike the original, additionally plays keystroke sounds
# while typing. For further information and usage examples see:
#
#     https://github.com/urbanware-org/typefx/blob/main/sound/README.md
#

import os
import random
import sys
import time

try:
    import playsound as ps
    playsound_installed = True
except:
    playsound_installed = False

try:
    from pydub import AudioSegment as pydub_seg
    from pydub.playback import play as pydub_play
    pydub_installed = True
except:
    pydub_installed = False

try:
    import simpleaudio as sa
    simpleaudio_installed = True
except:
    simpleaudio_installed = False

if not playsound_installed and not pydub_installed and \
   not simpleaudio_installed:
    raise Exception(
        "No supported sound module ('playsound', 'pydub' or "
        "'simpleaudio') found.")

dir_sounds = \
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "sounds")


def keystroke_sound(char="", static=True, sound_module="playsound"):
    if char == "":
        raise Exception("Keystroke must not be empty.")
    if sound_module == "":
        raise Exception("The sound module must not be empty.")

    if not os.path.exists(os.path.join(dir_sounds, "key_static.wav")):
        raise Exception(
            "Required sound file 'key_static.wav' is missing.")
    elif not os.path.exists(os.path.join(dir_sounds, "key_space.wav")):
        raise Exception(
            "Required sound file 'key_space.wav' is missing.")
    elif not os.path.exists(os.path.join(dir_sounds, "key_stroke1.wav")):
        raise Exception(
            "Required sound file 'key_stroke1.wav' is missing.")

    key_sound = ""
    if static:
        key_sound = os.path.join(dir_sounds, "key_static.wav")
    else:
        if char == " ":
            key_sound = os.path.join(dir_sounds, "key_space.wav")
        else:
            while not os.path.exists(key_sound):
                random.seed()
                key_random = random.randrange(1, 4)
                key_sound = \
                    os.path.join(
                        dir_sounds, "key_stroke" + str(key_random) + ".wav")

    if sound_module == "playsound":
        if not playsound_installed:
            raise Exception("The given sound module is not installed.")
        ps.playsound(key_sound, block=False)
    elif sound_module == "pydub":
        if not pydub_installed:
            raise Exception("The given sound module is not installed.")
        seg = pydub_seg.from_wav(key_sound)
        pydub_play(seg)
    elif sound_module == "simpleaudio":
        wave_object = sa.WaveObject.from_wave_file(key_sound)
        wave_object.play()
    else:
        raise Exception("The given sound module is not supported.")


def dynamic(string, delay_min=1, delay_max=100, sound_module="playsound"):
    """
        Print the input text "typewriter like" with a dynamic delay (in
        milliseconds).
    """
    if string == "":
        return

    try:
        delay_min = int(delay_min)
    except:
        raise Exception("The minimum delay must be an integer.")

    try:
        delay_max = int(delay_max)
    except:
        raise Exception("The maximum delay must be an integer.")

    if delay_max <= delay_min:
        raise Exception("The maximum delay must be greater than the "
                        "minimum delay.")
    if delay_min <= 0:
        raise Exception("The minimum delay must be greater than zero.")
    if delay_max <= 0:
        raise Exception("The maximum delay must be greater than zero.")

    for char in string:
        random.seed()
        wait = float(random.randrange(delay_min, delay_max)) / 1000
        keystroke_sound(char, False, sound_module)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(wait)


def static(string, delay=10, sound_module="playsound"):
    """
        Print the input text "machine like" with a static delay (in
        milliseconds).
    """
    if string == "":
        return

    try:
        delay = int(delay)
        wait = float(delay) / 1000
    except:
        raise Exception("The delay must be an integer.")

    if delay <= 0:
        raise Exception("The delay must be greater than zero.")

    delay = int(delay)
    wait = float(delay) / 1000
    for char in string:
        keystroke_sound(char, True, sound_module)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(wait)

# EOF
