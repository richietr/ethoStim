export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Thu July 21 15:05:00 2016' +%s); python trial.py -f Harlow -ps 5.png -ts 10 -d 8 -s 4 -fs right -x female -p 50 -sp gambusia -sl 328 -r 3 -cs R -fd -c -m $d
