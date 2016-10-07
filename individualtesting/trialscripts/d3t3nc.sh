export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue September 20 13:05:00 2016' +%s); python trial.py -f Lynn -ps 12.png -ts 6 -d 3 -s 3 -fs right -x female -p 50 -sp gambusia -sl TBD -r 6 -cs R -m $d
