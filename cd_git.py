#! /usr/bin/env python

import re
import subprocess as sub

WARNING = '\033[93m'
ENDC    = '\033[0m'

try:
    result = sub.check_output("git branch", stderr=sub.STDOUT, shell=True)
    match  = re.search('\*\s\w+', result)
    branch = match.group(0)

    if not branch == "* master":
        print; print WARNING + "WARNING: NOT ON MASTER BRANCH" + ENDC; print
except:
    pass
