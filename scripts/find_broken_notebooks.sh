#!/usr/bin/env bash

# Small script to find any notebooks that don't successfully run from top to
# bottom. Writes the name of each notebook found to stderr, any notebooks with
# errors are printed to stdout.
#
# You might use this script like so:
#
#     scripts/find_broken_notebooks.sh > broken_notebook_list.txt
#

for notebook in $(find content -name \*.ipynb); do
	echo processing $notebook >&2
	(jupyter nbconvert --execute --inplace $notebook >/dev/null 2>&1 || echo $notebook) &
done

wait
