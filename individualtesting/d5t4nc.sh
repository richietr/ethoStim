export DISPLAY=:0.0
d=$(date --date='TZ="US/Central" May 17 15:05:00 2016' +%s); python trial.py -f First -ps 5.png -ts 10 -d 5 -s 4 -fs right -x female -p 50 -sp gambusia -sl 413 -r 1 -m $d
