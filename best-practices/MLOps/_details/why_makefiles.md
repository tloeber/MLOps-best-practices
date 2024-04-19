# Pros

- allow steps to be run with a single command;
- allow defining *dependency* between steps (e.g., required background steps);
- create a central place where to *find* all setup commands.

# Cons

- Slight syntax differences. Most of this can be remediated though by following the tips and tricks below.

# Tips and tricks

- [Set bash as the shell to use at the top of each Makefile](https://github.com/tloeber/MLOps-template/blob/37fdb812d3b145dd372b9af18f1f3d532036a2af/Makefile#L1).
- Remaining difference in syntax from bash:
  - `:=` vs `=`: [The former is evaluated only once (at the first occurrence)](https://stackoverflow.com/questions/4879592/whats-the-difference-between-and-in-makefile).
  - `${my_var}` vs `${{my_var}}`: In the usual case where we are referring to *shell* variables, we need to use two curly currently braces.  Single curly braces refer to *make* variables (defined at the top of the Makefile).
  - If you get hung up in the make-specific syntax for a particularly tricky command, you can just put the code into a bash script and call it from the  Makefile. I think this is still better than forgoing the Makefile entirely, because it acts as an index of the important scripts that a user may want to call.
