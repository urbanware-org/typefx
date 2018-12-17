#!/bin/sh

# ============================================================================
# TypeFX - Typewriter effect text printer
# Android shell script function
# Copyright (C) 2018 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/typefx
# GitLab: https://gitlab.com/urbanware-org/typefx
# ============================================================================

version="1.0.0"

typefx() {
    delay=$1
    string=$2

    for char in $(echo "$string" | tr -c 1); do
        for lt in $(echo "$char" | tr -c 1); do
            echo "$lt\c"
            sleep $delay
        done
        echo " \c"
        sleep $delay
    done
    echo
}

# EOF
