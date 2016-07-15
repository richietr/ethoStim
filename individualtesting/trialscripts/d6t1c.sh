export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue July 19 9:05:00 2016' +%s); python trial.py -f Harlow -ps 5.png -ts 10 -d 6 -s 1 -fs right -x female -p 50 -sp gambusia -sl 328 -r 3 -cs R -fd -c -m $d
