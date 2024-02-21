#!/usr/bin/env bash

if ! which rst2html.py > /dev/null 2>&1 ; then
	echo 'ERROR: Missing required tool rst2html.py'
	exit 1
fi

rst2html.py --stylesheet style.css python.txt > python-assessment.html
