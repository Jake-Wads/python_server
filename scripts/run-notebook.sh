#!/usr/bin/env bash

usage() {
	cat <<-.
	$0 NOTEBOOK.ipynb

	Run a notebook in-place.
	.
}

if [[ -z $1 ]] ; then
	usage
	exit 1
fi

jupyter nbconvert --clear-output --inplace --execute $@
