export DISPLAY=:0.0
d=$(date --date='TZ="US/Central" May 13 11:05:00 2016' +%s); python trial.py -f First -ps 6.png -d 1 -s 2 -fs right-x female -p 50 -sp gambusia -sl 413 -r 1  -m $d
