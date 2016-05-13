export DISPLAY=:0.0
d=$(date --date='TZ="US/Central" May 16 15:05:00 2016' +%s); python trial.py -f First -ps 5.png -ts 10 -d 4 -s 4 -fs left -x female -p 50 -sp gambusia -sl 413 -r 1 -c -m $d
