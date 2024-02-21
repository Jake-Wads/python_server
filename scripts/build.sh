#!/usr/bin/env bash

cat <<-.
This script is deprecated, please use the makefile (make build) to organize the
build process.

See

	$ make help

.
exit 1

log() {
	echo "[$(date +'%X %x') build.sh] $@"
}

if [[ ! -f env/bin/activate ]] ; then
	log 'Error: could not find virtual environment activation script.'
	log 'Did you setup a virtual environment?'
	exit 1
fi

source env/bin/activate

set -e

if [[ -n $DEBUG ]] ; then
    set -x
fi

missing_utils_error() {
	cat <<-EOF
	This script requires several external programs:

	- rename
	- fd

	And the following pip packages to be installed in your virtual environment:

	- mkdocs
	- mkdocs-material
	- Pygments
	- pymdown-extensions

	If you are on MacOS, you can install all of these like so:

	    brew install rename fd
	    source env/bin/activate
	    python -m pip install -r requirements.txt
	    deactivate

	Please ensure these are all installed before continuing.
	EOF
}

check_prereqs() {
    prereqs=(rename fd mkdocs)
    for tool in ${prereqs[@]}; do

	    if ! which $tool >/dev/null 2>&1 ; then
		    log "Error: could not find $tool."
		    log
		    missing_utils_error
		    exit 1
	    fi
    done

	packages=(mkdocs mkdocs-material Pygments pymdown-extensions)
	installed_packages="$(python3 -m pip list | awk '{print $1}')"
    for package in ${packages[@]}; do
	    if ! grep "^$package$" >/dev/null 2>&1 <<< "$installed_packages" ; then
		    log "Error: missing pip package $package."
		    log
		    missing_utils_error
		    exit 1
	    fi
    done
}

ensure_clean_wd() {
	if [[ -n "$(git status --short)" ]] ; then
		cat <<-.
		It looks like you have unstaged changes. Please add any commit (or
		stash) any changes before running this script.
		.
		exit 1
	fi
}

gen_toc() {
	log '- Generating Table of Contents'
	python generate_toc.py > table_of_contents.md
}

clean_repo() {
    log '- Repo Cleanup'
	log '    - Removing built markdown and static files'
	rm -rf markdown site
    log '    - Removing .DS_Store files'
    fd -IH .DS_Store -x rm
    log '    - Removing .ipynb_checkpoints directories'
    fd -H --type d .ipynb_checkpoints -x rm -rf
    log '    - Removing html files'
    fd -e html --exclude theme/partials -x rm
    log '    - Removing R files'
    fd -e r -e rmd -x rm
    log '    - Replacing spaces in filenames with underscores'
    fd \\s -x rename 's/\s/_/g' {}
}

# Generates a config file that contains the names of all the notebooks in the
# repo, uses the config file with jupyter nbconvert to convert to markdown,
# then removes the config file.
# This is a little complex, but it's by far the fastest way that I've tried to
# go about converting all the notebooks to markdown.
convert_notebooks_to_markdown() {
    log '- Converting notebooks to markdown'
    rm -rf markdown
    mkdir markdown
    # jupyter nbconvert --clear-outputs --execute --to=markdown --output-dir=markdown --config=nbconvert_config.py
    fd -e ipynb |\
        perl -pe "s/^/'/; s/$/',/" |\
        sed -e '1s/^/c.NbConvertApp.notebooks = [/' -e '$s/$/]/' >\
        nbconvert_config.py
    jupyter nbconvert --to=markdown --output-dir=markdown --config=nbconvert_config.py
    rm nbconvert_config.py
}

copy_over_markdown() {
	log '- Copying over markdown files'
	fd -e md -x cp -v {} markdown >&2
	for file in $(cd grading && fd -e md -x basename {}) ; do
		rm markdown/$file
	done
}

copy_over_images() {
	log '- Copying over image files'
	mkdir -p markdown
	fd -e gif -e png -e jpg -e jpeg -x cp -v {} markdown/ >&2
}

build_static_site_directory() {
    log '- Building static site directory'

    log '    - Copying over logo and favicon'
    mkdir -p markdown/img
    cp -v logo.png markdown/logo.png >&2
    cp -v logo.png markdown/img/logo.png >&2
    cp -v favicon.ico markdown/img/favicon.ico >&2

    log '    - Copying over javascripts'
    cp -rv static-assets markdown/ >&2

    log '    - Creating index file'
    cat <<-EOF > markdown/index.md
	# Codeup Data Science

	$(< table_of_contents.md)
	EOF

    log '    - Building with mkdocs'
    mkdocs build
}

check_prereqs
ensure_clean_wd
gen_toc
clean_repo
convert_notebooks_to_markdown
copy_over_markdown
copy_over_images
build_static_site_directory

log '- Cleaning Up'
git checkout . && git clean -f >&2
