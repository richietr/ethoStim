export DISPLAY=:0.0
d=$(date --date='TZ="US/Central" May 14 11:05:00 2016' +%s); python trial.py -f First -ps 10.png -d 2 -s 2 -fs left -x female -p 50 -sp gambusia -sl 413 -r 1 -fd -m $d
