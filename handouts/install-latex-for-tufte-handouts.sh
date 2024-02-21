#!/usr/bin/env bash

# Short script to install all the necessary dependencies for rendering
# tufte-style handouts with r-markdown.
# Assumes a basic TeX installation with tlmgr available

Rscript -e 'install.packages(c("rmarkdown", "tufte"))'
sudo tlmgr install tufte
sudo tlmgr install hardwrap
sudo tlmgr install catchfile
sudo tlmgr install titlesec
sudo tlmgr install collection-fontsrecommended
sudo tlmgr install units
sudo tlmgr install morefloats
