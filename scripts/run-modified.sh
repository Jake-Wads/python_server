#!/usr/bin/env bash

usage() {
	cat <<-.
	$0

	Runs any jupyter notebooks that git thinks have been modified since the last
	commit.
	.
}

if [[ $1 == help || $1 == -h || $1 == --help ]] ; then
	usage
	exit 1
fi

notebooks=`git status --porcelain | egrep '^\sM' | grep '\.ipynb$' | awk '{print $2}'`

if [[ -z $notebooks ]] ; then
	echo 'No modified notebooks found.'
	echo 'Exiting...'
	exit
fi

jupyter nbconvert --clear-output --inplace --execute $notebooks
