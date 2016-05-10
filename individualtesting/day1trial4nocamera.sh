#!/bin/bash
d=$(date --date='TZ="US/Central" May 10 19:05:00 2016' +%s); python trial.py -f Fourth -ps 10.png -d 1 -s 4 -fs left -x male -p 50 -sp gambusia -sl 0123 -r 1 -m $d
