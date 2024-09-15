# Keyboard shortcuts

## Customizing keyboard modifiers for Windows or Linux users

To get the most similar experience to Windows or Linux, swap control and command keys.

### Builtin keyboard

- Swap `cmd` and `ctrl` modifiers

### External non-Apple keyboard

 If using Windows keyboard, an additional complication  is introduced: By default, the location of option and command is flipped (see first and second column). To fix this, remap keys (Settings/Keyboard/Keyboard Shortcuts/Modifier Keys) in 2nd columnn to those in 3rd column:

| Windows | Mac default | Mac remapped |
| --- | --- | --- |
| Ctrl | Ctrl | Cmd |
| Win | Cmd | Option |
| Alt | Option | Ctrl |
||||

### Default shortcuts to free up

- mission control (second on that has sub-bullets - the top one is equivalent to alt+tab on Windows, whereas the second one switches desktops & spaces)

### Remaining Differences in Shortcuts

On Windows  keyboard with above remappings:
| Category| Action | Windows | Mac default | Mac Custom | Mac Default | Notes |
| ---| --- | --- | --- | ---- | --- | --- |
| Navigation | Switch Window | Alt + Tab | Ctrl + Tab ||||
| | Switch Windows (same app) | - | Ctrl + ~ ||||
| | Hide/unhide current Window | Win + down / Alt + tab | Ctrl + H ? Ctrl + tab ||||
| | Minimize/restore current Window | Win + down / Alt + tab | Ctrl + M / Ctrl + tab + option (release tab before pressing option, release cmd before option) ||||
| | Show desktop / restore folders | Win + D / Win + D | ? ||||
| | Show all Windows ("Mission Control") | Win + tab| Alt + Up | Win + tab (add shift to go back)*|| On Mac, can't use arrows + Enter to select a window. Only can do control + down to go back to original window. |
|| Select Menu bar | Alt + underlined letter | Ctrl + F2 | Win + M || Change under Shortcuts/keyboard/Move focus to menu bar |
||||||||
| Browser | Go back | Alt + left | Ctrl + left ||||
| | Cycle through tabs | Ctrl + PgUp/Down | Alt + PgUp/Dn ||| Doesn't work on Safari |
| |||||||
| |||||||
| Text Editing | Delete word | Ctrl + Backspace | Win + Backspace ||||
| | Go one word left/right | Ctrl + left/right | Win + left/right ||||
| | Go to beginning/end of line | Home/end | Ctrl + left/right ||||
||||||||
| Other | right-click | "menu key" | alt + click ||||
| | Open selected file | Enter | Ctrl + O ||||

- Set "Application  Windows to Alt + Shift + tab to be able to go back.

# Use bash instead of zsh

- Rationale: Consistency with Linux dev environment
- Procedure:
  - Download recent version bash using homebrew (builtin version is ancient)
  - Add its location to /etc/shells
  - Run `chsh -s $INSTALL_LOCATION`

# Other

- Turn off "natural scrolling" in trackpad options. Otherwise, mouse wheel will scroll into the opposite direction as on Windows.
