#!/bin/bash
cd src
pdflatex --shell-escape -synctex=1 -interaction=nonstopmode book
makeindex book.idx -s StyleInd.ist
biber book
pdflatex --shell-escape -synctex=1 -interaction=nonstopmode book
pdflatex --shell-escape -synctex=1 -interaction=nonstopmode book
