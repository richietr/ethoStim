export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Fri September 23 9:05:00 2016' +%s); python trial.py -f Lynn -ps 10.png -ts 5 -d 6 -s 1 -fs right -x female -p 50 -sp gambusia -sl TBD -r 6 -cs R -m $d
