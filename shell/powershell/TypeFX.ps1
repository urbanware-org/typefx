# ============================================================================
# TypeFX - Typewriter effect text printer
# PowerShell script function
# Copyright (C) 2019 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/typefx
# GitLab: https://gitlab.com/urbanware-org/typefx
# ============================================================================

$TypeFxVersion = "1.0.0"

Function Type-Static {
    [Int32]$Delay = $args[0]
    [String]$String = $args[1]

    For ($i = 0; $i -lt $String.Length; $i++) {
        Write-Host $String[$i] -NoNewLine
        Start-Sleep -Milliseconds $Delay
    }
}
