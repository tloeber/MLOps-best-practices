# Keyboard shortcuts

## Customizing keyboard modifiers for Windows or Linux users

To get the most similar experience to Windows or Linux, swap control and command keys.

### Builtin keyboard

- Swap `cmd` and `ctrl` modifiers

### External non-Apple keyboard

 If using Windows keyboard, an additional complication  is introduced: By default, the location of option (Win) and command is flipped (see first and second column below). To fix this, remap keys (Settings/Keyboard/Keyboard Shortcuts/Modifier Keys) in 2nd columnn to those in 3rd column:

| Windows keyboard | Mac keyboard - default | Mac keyboard - remapped |
| --- | --- | --- |
| Ctrl | Ctrl | Cmd |
| Win | Cmd | Option |
| Alt | Option | Ctrl |
||||

### Default shortcuts to free up

- mission control: Uncheck to not switch spaces and desktops (I just switch between applications using cmd + tab, and use separate screens for windows between which I frequently go back and forth).
- minimize window (causes trouble going back to it (have to remember it's minimized and press Win key, and then release it just in time). So "hide" instead (Ctrl + H))
- Don't cause problems, but free up to avoid small chance of interference with custom shortcuts:
  - "Turn dock hiding on/off"
  - "Show Launchpad"

### Shortcuts to modify

- Set "Mission Control / Application  Windows" to Alt + W (to be able to display all windows of an app)

### Remaining Differences in Shortcuts

Do: Change all shurtcuts in the "Mac custom" column.

Note: On Windows keyboard (i.e. "Ctrl" refers to the key labeled "Ctrl", not "cmd" to which it is mapped) with above remappings.

| Category| Action | Windows | Mac default | Mac Custom | Notes |
| ---| --- | --- | --- | ---- | --- |
| Navigation | Switch Window | Alt + Tab | Ctrl + Tab |||
| | Switch Windows (same app) | - | Ctrl + ~ |||
| | Hide/unhide current Window | Win + down / Alt + tab | Ctrl + H / Ctrl + tab |||
| | ~~Minimize/restore current Window~~ | ~~Win + down / Alt + tab~~ | ~~Ctrl + M / Ctrl + Win + tab (release tab before pressing Win, release cmd before Win)~~ | ~~None (disabled); use Ctrl + H / Ctrl + tab instead~~ ||
| | Show desktop / restore folders | Win + D | F11 || Don't need to memorize |
| | Show all Windows ("Mission Control") | Win + tab| Alt + Up | Win + tab (add shift to go back)*| On Mac, can't use arrows + Enter to select a window. Only can do control + down to go back to original window. |
|| Select Menu bar | Alt + underlined letter | Ctrl + F2 | Win + M | Change under Shortcuts/keyboard/Move focus to menu bar |
|||||||
| Browser | Go back | Alt + left | Ctrl + left |||
| | Cycle through tabs | Ctrl + PgUp/Down | Alt (+ shift) + tab (all browsers); Alt + PgUp/Dn (more convenient but doesn't work on Safari) |||
| ||||||
| Text Editing | Delete word | Ctrl + Backspace | Win + Backspace |||
| | Go one word left/right | Ctrl + left/right | Win + left/right |||
| | Go to beginning/end of line | Home/end | Ctrl + left/right |||
|||||||
| Other | right-click | "menu key" | alt + click |||
| | Open selected file | Enter | Ctrl + O |||

# Other config changes

- Turn off "natural scrolling" in trackpad options. Otherwise, mouse wheel will scroll into the opposite direction as on Windows.
- Desktop & Dock / Mission Control: Disable "displays have separate spaces" and "automatically rearrange spaces ..." and "when switching to an application..." to avoid using spaces (the first one is most important, not sure how much each of the others helps).

# Other customizations

## Use bash instead of zsh

- Rationale: Consistency with Linux dev environment
- Procedure:
  - Download recent version of bash using homebrew (builtin version is ancient)
  - Add its location to /etc/shells
  - Run `chsh -s $INSTALL_LOCATION`

# Docking station

Get a *thunderbolt* docking station, so you don't need to install Displaylink (which is external software) to support multiple displays.
