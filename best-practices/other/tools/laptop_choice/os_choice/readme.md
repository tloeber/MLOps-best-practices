## Mac vs PC (vs Linux)

- Challenge: switching has big impact on productivity, in particular for developers, since they tend to rely heavily on keyboard shortcuts for productivity
- Implications:
  - If at all possible, give employees a choice over desired OS.
  - if standardization is required, make this as easy as possible:
    - Collect pain points developers usually face in switching, and crowd-source solutions in company wiki
      - In particular, how can we make productivity shortcuts less platform-dependent? See [here](../../../../productivity/keyboard-shortcuts/readme.md) for my approach.
      - Mac:
        - [Customize keyboard modifying keys](Mac/readme.md).
        - Due to the lower customizability of shortcuts on MacOS, we **need a third-party program** (e.g., Magnet, Rectangle, or [Karabiner](https://karabiner-elements.pqrs.org/)) for customizing remaining shortcuts. While we generally don't want developers to install random programs, it is essential that wemake sure there is an approved program for remapping keyboard shortcuts, since these are essential for developer productivity.
          - Limitations of builtin shortcuts (as MacOS Sequia (2024)):
            - Most importantly: Can't create a general shortcut to move window to another screen. While you can create a custom shortcut to move a window to a specific display, you have to hard-code the display name. Thus, you would have to create different shortcuts for different docking stations you may connect to. (If you could customize the name of the external displays, you could make the names identical and use the same shortcut, but unfortunately the display names can't be edited.)
            - Less important but inconvenient: Only supports splitting windows in halfs and quarters. In my case, I have a large center display, and use Magnet to be able to split it in 2/3 (for the IDE) and 1/3 for, say, a browser. This also gives me the option to split it in thirds and look at three tall windows next to each other.
