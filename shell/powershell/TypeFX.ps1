# ============================================================================
# TypeFX - Typewriter effect text printer
# PowerShell script function
# Copyright (C) 2020 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/typefx
# GitLab: https://gitlab.com/urbanware-org/typefx
# ============================================================================

$TypeFxVersion = "1.1.1"

Function Type-Dynamic([Int32]$DelayMin, [Int32]$DelayMax, [String]$String) {
    For ($i = 0; $i -lt $String.Length; $i++) {
        Write-Host $String[$i] -NoNewLine
        $Delay = Get-Random -Minimum $DelayMin -Maximum $DelayMax
        Start-Sleep -Milliseconds $Delay
    }
    Write-Host
}

Function Type-Static([Int32]$Delay, [String]$String) {
    For ($i = 0; $i -lt $String.Length; $i++) {
        Write-Host $String[$i] -NoNewLine
        Start-Sleep -Milliseconds $Delay
    }
    Write-Host
}
