# *TypeFX* with keystroke sounds

**Table of contents**
*   [Definition](#definition)
*   [Details](#details)
*   [Usage](#usage)

----

## Definition

This directory contains an **experimental** version of the *TypeFX* module, which, unlike the original, additionally plays keystroke sounds while typing.

I haven't done much with sound modules in *Python* (or at all) before, so this was a first attempt. Since then, I haven't had the time or leisure to play around with these sound modules either. As mentioned above, this was an experiment, so it is uncertain whether I will enhance or modify it at all.

[Top](#typefx-with-keystroke-sounds)

## Details

So far, the script supports the three sound modules *playsound*, *pydub* and *simpleaudio*.

However, there were some issues with *pydub* (including *ffmpeg* crashes), which have not been investigated further and it is recommended to use one of the others instead.

Depending on the sound module you are using, the script may crash or does not play the sounds properly. Therefore, you should first try out which module works best for you.

The script path contains the sub-directory `sounds`. Inside this directory there are five files:

*   `key_static.wav` (used for all characters for static "machine like" mode)
*   `key_space.wav` (used for spaces for dynamic "typewriter like" mode, only)
*   `key_stroke1.wav` (one of the random sounds used for dynamic "typewriter like" mode, only)
*   `key_stroke2.wav` (one of the random sounds used for dynamic "typewriter like" mode, only)
*   `key_stroke3.wav` (one of the random sounds used for dynamic "typewriter like" mode, only)

The files `key_static.wav` and `key_space.wav` are required.

For the keystrokes at least `key_stroke1.wav` must exist, `key_stroke2.wav` and `key_stroke3.wav` are optional. However, it is recommended to provide all of them. Further keystroke sounds e.g. `key_stroke4.wav` are not supported, so there is a maximum of three sounds.

[Top](#typefx-with-keystroke-sounds)

## Usage

The function call itself is identical to that of the usual *TypeFX* methods, but with an additional parameter for the preferred sound module.

### Default behavior

If no specific sound module is given, the script will use *playsound* by default.

```python
typefx.static(string, delay=10)
```
```python
typefx.dynamic(string, delay_min=1, delay_max=100)
```

### Module *playsound*

Even though this module is the default one, it can also be given explictily.

```python
typefx.static(string, delay=10, sound_module="playsound")
```
```python
typefx.dynamic(string, delay_min=1, delay_max=100, sound_module="playsound")
```

### Module *pydub*

Simply change (or add) the corresponding `sound_module` parameter:

```python
typefx.static(string, delay=10, sound_module="pydub")
```
```python
typefx.dynamic(string, delay_min=1, delay_max=100, sound_module="pydub")
```

### Module *simpleaudio*

Simply change (or add) the corresponding `sound_module` parameter:

```python
typefx.static(string, delay=10, sound_module="simpleaudio")
```
```python
typefx.dynamic(string, delay_min=1, delay_max=100, sound_module="simpleaudio")
```

[Top](#typefx-with-keystroke-sounds)
