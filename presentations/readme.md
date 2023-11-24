# How to make slides from Jupyter notebook

# Microsoft extension for VSCode

- Docs: <https://github.com/microsoft/vscode-jupyter-slideshow>
- Pros:
  - Can use IDE
- Cons:
  - One extra click for each cell (which adds up) to set slide type
  - Have to convert to HTML in order to generate slides, so can't generate slides on the fly. That said, when converting a large notebook to a slideshow for the first time, it is possible to set all cells to "slide" by editing the metadata (click "edit cell tags (JSON)") and using search/replace)

# RISE extension

- Docs:
  - for Jupyter <7: <https://rise.readthedocs.io/en/latest/>
  - for Jupyter>=7 and Jupyter Lab: <https://github.com/jupyterlab-contrib/rise>
- Pros:
  - Since it's running in the browser, you can set the view so that slight type drop-down automatically shows up for every cell, so it is less of a hassle to set (saves one click for every cell)
    - Can present right from notebook without conversion to HTML, and can even edit presentation on the fly (propagates to notebook).
- Cons:
  - Doesn't work with VS Code
