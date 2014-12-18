#! /usr/bin/env python

import re
import subprocess as sub

try:
    result = sub.check_output("git branch", stderr=sub.STDOUT, shell=True)
    match  = re.search('\*\s\w+', result)
    branch = match.group(0)

    if not branch == "* master":
        print "NOT ON MASTER"
except:
    pass
