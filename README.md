# The innoficial songbook for the Line associations at Mäladalens University
To compile this work we suggest using [Visual Studio Code](https://code.visualstudio.com/) and the extension [LaTeX Workshop](https://github.com/James-Yu/LaTeX-Workshop) Along with [Miktex](https://miktex.org/download).

Setup.sty contains several functions and packages used throughout the work. The important ones are shown off in either main.tex or in Example.tex

AlphaBetatoc.py orderes the subsections in main.toc. Needs to be run after the main builder and comes into effect after the next build.

To set this up automatically you can add this behaviour into the [LaTeX Workshop](https://github.com/James-Yu/LaTeX-Workshop) settings.json. 

Add the tool

{
    "name": "Python Script to Sort Table of Contect",
    "command": "python",
    "args": [
    "%DIR%/AlphaBetatoc.py",
    ],
    "env": {}
}

and the recipe (Note place this first in the list to make it default)

{
    "name": "pdfLaTeX+Python+pdfLaTeX",
    "tools": [
    "pdflatex",
    "Python Script to Sort Table of Contect",
    "pdflatex",
    ]
}