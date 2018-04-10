#!/bin/bash

# ============================================================================
# TypeFX - Typewriter effect text printer
# Bash shell script function
# Copyright (C) 2018 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/typefx
# ============================================================================

typefx() {
    delay=$1
    string=$2

    for char in $(seq 0 $(expr length "${string}")); do
        echo -n "${string:$char:1}"
        sleep $delay
    done
    echo
}

# EOF
