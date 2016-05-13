export DISPLAY=:0.0
d=$(date --date='TZ="US/Central" May 19 15:05:00 2016' +%s); python trial.py -f First -ps 0.png -ts 0 -d 7 -s 4 -fs both -x female -p 0 -sp gambusia -sl 413 -r 1 -fd -c -m $d
