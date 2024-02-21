#!/usr/bin/env bash

# script that allows renaming a curriculum file and will update the name in the
# table of contents

if [[ -z $1 ]] ; then
	cat <<-.
	$0 path_to_notebook_or_directory
	.
	exit
fi

dir=$1

for path in $(find $dir) ; do
	[[ -d $path ]] && continue
	file=$(basename $path)
	[[ $file == .gitignore ]] && continue

	extension=${file##*.}
	basename=${file%.*}

	if grep -q $basename table-of-contents.yml ; then
		read -ep "Rename $basename: " new_name
		rename "s/$basename/$new_name/" $path
		perl -i -pe "s/$basename/$new_name/g" table-of-contents.yml
	fi
done

