# *TypeFX*

**Table of contents**
*   [Definition](#definition)
*   [Details](#details)
*   [Shell alternative](#shell-alternative)
*   [Requirements](#requirements)
*   [Contact](#contact)
*   [Useless facts](#useless-facts)

----

## Definition

The *TypeFX* module allows printing a string with a user-defined delay after each character.

[Top](#typefx)

## Details

There are two types of delays:

*   **static**<br>Prints the output "typically machine-like", character by character at the same speed.
*   **dynamic**<br>Prints the output "typewriter-like" as if a person was typing (available in the *Python* module, only).

[Top](#typefx)

## Shell alternative

In case the "machine like" type effect should be used in a shell script, it would be quite inconvenient to use this *Python* module every time when printing a text on the shell.

However, such an effect can also be produced using shell commands. Below you can find a code snippet containing a shell function for that purpose.

### *Bash*

The following code was developed on the *Bash* shell, which is the default shell on many *Unix*-like systems (or at least *Linux* distributions). It may also work with other shells, however, there is no guarantee for that.

```bash
#!/bin/bash

typefx() {
    delay=$1
    string=$2

    for char in $(seq 0 $(expr length "${string}")); do
        echo -n "${string:$char:1}"
        sleep $delay
    done
    echo
}

typefx 0.01 "This is a simple text printed on the shell."
```

### Terminal emulator on *Android*

While waiting, I wanted to use the time for something "useful", so I wrote a *TypeFX* script on the terminal emulator of my smartphone.

However, even though this runs on *Android* (at least on version 6 and 7), it does not run on a *Linux* system, because of `tr` is missing an argument.

```sh
#!/bin/sh

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

typefx 0.01 "This is a simple text printed on the shell."
```

[Top](#typefx)

## Requirements

In order to use *TypeFX*, the *Python* framework must be installed on the system.

Depending on which version of the framework you are using:

*   *Python* 2.x (version 2.7 or higher is recommended, may also work with earlier versions)
*   *Python* 3.x (version 3.2 or higher is recommended, may also work with earlier versions)

[Top](#typefx)

## Contact

Any suggestions, questions, bugs to report or feedback to give?

You can contact me by sending an email to <dev@urbanware.org>.

[Top](#typefx)

## Useless facts

*   The project name is an abbreviation for *Type Effects*.
*   The first version uploaded on *GitHub* was *TypeFX* 1.1.1 built on March 31<sup>st</sup>, 2015.
*   Before uploading, the project has neither been changed nor even touched for almost three years.
*   The module for *Python* 3 was created by converting the *Python* 2 module using the *2to3* tool. However, both files are identical except for the shebang.

[Top](#typefx)
