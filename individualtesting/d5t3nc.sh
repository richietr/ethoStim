export DISPLAY=:0.0
d=$(date --date='TZ="US/Central" May 16 13:05:00 2016' +%s); python trial.py -f First -ps 12.png -d 2 -s 1 -fs none -x female -p 50 -sp gambusia -sl 413 -r 1 -m $d
