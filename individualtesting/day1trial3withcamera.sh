#!/bin/bash
d=$(date --date='TZ="US/Central" May 10 17:05:00 2016' +%s); python trial.py -f Third -ps 12.png -d 1 -s 3 -fs right -x male -p 50 -sp gambusia -sl 0123 -r 1 -c -m $d
