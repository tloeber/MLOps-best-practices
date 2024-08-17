# Navigating windows
|| Windows & Linux | Mac |
| --- | --- | --- |
| Toggle fullscreen | | |
| Move to other monitor |||
| Move & resize window to left/right half of screen |||

# IDEs

- VSCode: See the settings file in [my utils_and_configs repo](https://github.com/tloeber/utils_and_configs/blob/main/IDEs/VSCode/keybindings/keybindings.json)

# Constraints

## Keys - Hardcoded OS differences

### Note on Terminology

**Using standard Windows Keyboard terms, with `ctrl` and `cmd` switched for Mac for maximum similarity to Windows and Ubuntu (link)! Thus,  for MacOS `ctrl` refers to `cmd`, not `ctrl`.** While this is not ideal, the goal is to think about shortcuts in terms of these standardized terms, ignoring the idiosyncrasies of specific operating systems.

### Keys not available everywhere for custom shortcuts

Judged by VSCode shortcuts - but can try using these for *other* shortcuts

- windows: super -> Try to use it in MacOS to do the same it does on Windows - namely moving and resizing windows!

### Unavailable shortcuts

#### with left/right arrow

Reserved because these are the standard ways to navigate and edit text, so we don't want to change these for a single application.
Todo: Check if can leverage Mac's system for Win & Ubuntu, because not needing  home/end keys would be nice!

- ubuntu & win: ctrl, shift
- mac:   ctr,  super,

- **Remaining: Alt**.  But can also use *multiple* modifier keys.
-> Use Alt + left/right for moving between editor tabs.
-> Use Alt + *shift* + left/right for moving between editor tab *groups*.
-> Use Ctrl + Alt + left/right/etc to move between screens, or Super + left/right if it can be configured on MacOS

### Impractical Shortcuts

If you're not using a modifier key, VSCode may prevent you from typing normal text:

- e.g., L + left
If you type "L", it will block and wait whether you also press "left" .
Solution:
**- Always add a proper modifier (NOT shift, except for keys that don't have shift ability** (up/down/left/right etc).
- Remember that **if we define "double" shortcuts, the first stroke (e.g., ctrl + K), this eliminates ability to use keyboard combination of the first stroke *by itself*** because the application keeps waiting for second stroke. Double stroke-shortcuts are still a good solution to provide something akin to a new namespace for a related set of functionality (if running out of good shortcuts).

## Shortcuts not changeable

Note that all these examples result from switching ctrl and cmd on MacOS! However, *without* doing so, there are much more dissimilarities for everyday tasks (e.g.,  cmd + S for saving, cmd + O for open, cmd + T for new tab, cmd + R for reloading Page, etc.)

### Browser

go back:

- Windows/Ubuntu: alt + left
- MacOS: ctrt + left

## Navigating windows

Move & resize window to left/right half/quarter of screen: Super + left/right/up/down
Move to other monitor: Super + *shift* + left/right/up/down
Toggle fullscreen: Super + left/right/up/down
Switch between windows (configurable in Ubuntu):

- Windows: Alt + tab (configurable using Microsoft PowerToys)
- MacOs: Ctrl + tab (double check if configurable)

# Using modifier keys to group shortcuts

Default for most common operations, especially editing: Ctrl
 Navigating windows: ctrl + alt ?
 debugging: alt?
