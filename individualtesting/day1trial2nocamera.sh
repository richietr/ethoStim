#!/bin/bash
d=$(date --date='TZ="US/Central" May 10 15:05:00 2016' +%s); python trial.py -f Second -ps 12.png -d 1 -s 2 -fs right -x male -p 50 -sp gambusia -sl 0123 -r 1 -fd -m $d
