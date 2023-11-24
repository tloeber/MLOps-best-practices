# How to make slides from Jupyter notebook

# Microsoft extension for VSCode

This is my **preferred choice** so far.

- Docs: <https://github.com/microsoft/vscode-jupyter-slideshow>
- Pros:
  - Can use IDE
- Cons:
  - ~~One extra click for each cell (which adds up) to set slide type~~
    - Resolved: [Can create VSCode keyboard shortcut for "switch slide type"](https://github.com/tloeber/utils_and_configs/blob/046e7053601b7faabc79b574be0a6a84239b016b/IDEs/VSCode/keybindings/keybindings.json#L674).
  - Have to convert to HTML in order to generate slides, so can't generate slides on the fly. That said, when converting a large notebook to a slideshow for the first time, it is possible to set all cells to "slide" by editing the metadata (click "edit cell tags (JSON)") and using search/replace)

# RISE extension

- Docs:
  - for Jupyter <7: <https://rise.readthedocs.io/en/latest/>
  - for Jupyter>=7 and Jupyter Lab: <https://github.com/jupyterlab-contrib/rise>
- Pros:
  - ~~Since it's running in the browser, you can set the view so that slide-type drop-down automatically shows up for every cell, so it is less of a hassle to set (saves one click for every cell).~~
    - Not an advantage relative to VSCode, which allows setting custom shortcut for this task. (Might actually be a disadvantage, depending on whether you can also set a shortcut for this in a browser notebook).
  - Can present right from notebook without conversion to HTML, and can even edit presentation on the fly (propagates to notebook).
- Cons:
  - Doesn't work with VS Code
