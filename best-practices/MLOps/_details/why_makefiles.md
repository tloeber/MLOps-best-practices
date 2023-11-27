- Pros:
  - allow steps to be run with a single command;
  - allow defining *dependency* between steps (e.g., required background steps);
  - create a central place where to *find* all setup commands.

- Cons:
  - Commands run in sh vs bash, giving rise to some unexpected behavior (especially around things such as quoting and variable substitution).
    - Workaround: If running into problems, simply put commands in a bash script and call from the makefile. (Note that this still allows us to retain the third benefit of makefiles, namely using the makefile as a central place referencing all the bash script that a user may need to call directly, even if these scripts are organized into different subdirectories.)
