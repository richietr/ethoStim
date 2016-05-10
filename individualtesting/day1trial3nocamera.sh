#!/bin/bash
d=$(date --date='TZ="US/Central" May 5:05:00 2016' +%s); python trial.py -f Third -ps 6.png -d 1 -s 3 -fs right -x male -p 50 -sp gambusia -sl 0123 -r 1 - fd -m $d
