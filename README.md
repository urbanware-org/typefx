# *TypeFX*

**Table of contents**
*   [Definition](#definition)
*   [Details](#details)
*   [Shell alternatives](#shell-alternatives)
*   [Requirements](#requirements)
*   [Contact](#contact)
*   [Useless facts](#useless-facts)

----

## Definition

The *TypeFX* module allows printing a string with a user-defined delay after each character.

:arrows_clockwise: If you are also interested in a character flipping effect text printer module, you can find it [here](https://github.com/urbanware-org/flipfx).

[Top](#typefx)

## Details

With the *Python* modules, there are two types of delays.

### Static

Prints the output "typically machine-like", character by character at the same speed.

### Dynamic

Prints the output "typewriter-like" as if a person was typing. This method is available in the *Python* modules and the *PowerShell* code, only.

### **Usage examples**

#### Code

Notice that the delays must be given in milliseconds.

```python
import typefx
typefx.static("This is the static \"typically machine-like\" output effect.", 10)
typefx.dynamic("This is the dynamic \"typewriter-like\" output effect.", 20, 300)
```

#### Output

<img src="https://raw.githubusercontent.com/urbanware-org/typefx/master/gif/typefx.gif" alt="TypeFX sample output" width="64%">

[Top](#typefx)

## Shell alternatives

In case the effects should be used in a shell script, it would be quite inconvenient to use this *Python* module every time when printing a text on the shell.

However, such effects can also be produced using shell commands. Below you can find some code snippets for various shells.

Below you can find code for the following:

*   [*Bash*](#bash)
*   [*Android*](#terminal-emulator-on-android) terminal emulator
*   [*PowerShell*](#powershell)

### *Bash*

The following code was developed on the *Bash* shell, which is the default shell on many *Unix*-like systems (or at least *Linux* distributions). It may also work with other shells, however, there is no guarantee for that.

Notice that unlike the *Python* scripts, the delay range must be given in seconds instead of milliseconds and the delay must be given before the string. Furthermore, the following script provides the static "typically machine-like" output effect, only.

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

Notice that unlike the *Python* scripts, the delay range must be given in seconds instead of milliseconds and the delay must be given before the string. Furthermore, the following script provides the static "typically machine-like" output effect, only.

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

### *PowerShell*

Here is the *PowerShell* code for both effects. As in the *Python* scripts, the delay must be given in milliseconds, but the delays must be given before the string.

```powershell
Function Type-Dynamic {
    [Int32]$DelayMin = $args[0]
    [Int32]$DelayMax = $args[1]
    [String]$String = $args[2]

    For ($i = 0; $i -lt $String.Length; $i++) {
        Write-Host $String[$i] -NoNewLine
        $Delay = Get-Random -Minimum $DelayMin -Maximum $DelayMax
        Start-Sleep -Milliseconds $Delay
    }
    Write-Host
}

Function Type-Static {
    [Int32]$Delay = $args[0]
    [String]$String = $args[1]

    For ($i = 0; $i -lt $String.Length; $i++) {
        Write-Host $String[$i] -NoNewLine
        Start-Sleep -Milliseconds $Delay
    }
    Write-Host
}

Type-Static 10 'This is the static "typically machine-like" output effect.'
Type-Dynamic 20 300 'This is the dynamic "typewriter-like" output effect.'
```

[Top](#typefx)

## Requirements

In order to use the *TypeFX* scripts in *Python*, the framework must be installed on the system.

Depending on which version of the framework you are using:

*   *Python* 2.x (version 2.7 or higher is recommended, may also work with earlier versions)
*   *Python* 3.x (version 3.2 or higher is recommended, may also work with earlier versions)

[Top](#typefx)

## Contact

Any suggestions, questions, bugs to report or feedback to give?

You can contact me by sending an email to [dev@urbanware.org](mailto:dev@urbanware.org) or by opening a *GitHub* issue (which I would prefer if you have a *GitHub* account).

[Top](#typefx)

## Useless facts

*   The project name is an abbreviation for *Type Effects*.
*   The first version uploaded on *GitHub* was *TypeFX* 1.1.1 built on March 31<sup>st</sup>, 2015.
*   Before uploading, the project has neither been changed nor even touched for almost three years.

[Top](#typefx)
