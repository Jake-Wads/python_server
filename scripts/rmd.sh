#!/usr/bin/env bash

if [[ -z "$1" ]] ; then
    echo 'Please provide a filename.'
    exit 1
fi

# Rscript -e "rmarkdown::run('$1')" # for shiny apps

if [[ -n $2 ]] ; then
    Rscript -e "rmarkdown::render('$1', output_file = '$2', output_dir = '$(dirname $2)')"
else
    Rscript -e "rmarkdown::render('$1')"
fi
