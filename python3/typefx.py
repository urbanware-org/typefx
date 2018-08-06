#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================================================
# TypeFX - Typewriter effect text printer
# Copyright (C) 2018 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/typefx
# GitLab: https://gitlab.com/urbanware-org/typefx
# ============================================================================

__version__ = "1.1.2"

import random
import sys
import time


def dynamic(string, delay_min=1, delay_max=100, use_utf8=True):
    """
        Print the input text "typewriter like" with a dynamic delay (in
        milliseconds).
    """
    if delay_max <= delay_min:
        raise Exception("The maximum delay must be greater than the "
                        "minimum delay.")
    if delay_min <= 0:
        raise Exception("The minimum delay must be greater than zero.")
    if delay_max <= 0:
        raise Exception("The maximum delay must be greater than zero.")

    if use_utf8:
        string = string.encode("utf8", "ignore")

    delay_min = int(delay_min)
    delay_max = int(delay_max)
    for char in string:
        random.seed()
        wait = float(random.randrange(delay_min, delay_max)) / 1000
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(wait)


def static(string, delay=10, use_utf8=True):
    """
        Print the input text "machine like" with a static delay (in
        milliseconds).
    """
    if delay <= 0:
        raise Exception("The delay must be greater than zero.")

    if use_utf8:
        string = string.encode("utf8", "ignore")

    delay = int(delay)
    wait = float(delay) / 1000
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(wait)

# EOF
