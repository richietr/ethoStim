export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Fri August 12 13:05:00 2016' +%s); python trial.py -f Heidi -ps 10.png -ts 5 -d 5 -s 3 -fs right -x female -p 50 -sp gambusia -sl TBD -r 4 -cs R -fd -c -m $d
