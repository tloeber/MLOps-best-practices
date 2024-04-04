- Pros:
  - allow steps to be run with a single command;
  - allow defining *dependency* between steps (e.g., required background steps);
  - create a central place where to *find* all setup commands.

- Cons:
  - Slight syntax differences. Most of this can be remediated though by [setting bash as the shell to use at the top of each Makefile](https://github.com/tloeber/MLOps-template/blob/37fdb812d3b145dd372b9af18f1f3d532036a2af/Makefile#L1).
