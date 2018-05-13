## PowerShell volume controls
Exposes audio controls (volume and mute) via PowerShell, and toggles the mute switch based on whether the computer is locked or not. Used in the office to mute my desktop (and thus notifications) when I step away from it.

### `scripts/volume.psm1`
Integrates audio controls through the commands `Get-AudioVolume`, `Set-AudioVolume`, `Get-AudioMuteState` and `Set-AudioMuteState`.

### `tasks/`
Two Windows scheduled tasks which trigger at lock & unlock, controlling the computer's mute state. To install: copy the scripts from `scripts/` into `C:\Program Files\Scripts` and import the tasks from `tasks/` via "Task Scheduler" > right-hand menu > "Import...".
