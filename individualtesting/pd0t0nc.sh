export DISPLAY=:0.0
d=$(date --date='TZ="US/Central" May 11 13:05:00 2016' +%s); python trial.py -f First -ps 10.png -d 1 -s 1 -fs both -x male -p 50 -sp gambusia -sl 0123 -r 1 -fd -m $d
