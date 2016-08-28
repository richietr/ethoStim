export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Mon August 15 17:05:00 2016' +%s); python trial.py -f Heidi -ps 12.png -ts 6 -d 8 -s 5 -fs right -x female -p 50 -sp gambusia -sl TBD -r 4 -cs R -fd -c -m $d
