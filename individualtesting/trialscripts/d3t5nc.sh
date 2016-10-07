export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue September 20 17:05:00 2016' +%s); python trial.py -f Lynn -ps 10.png -ts 5 -d 3 -s 5 -fs right -x female -p 50 -sp gambusia -sl TBD -r 6 -cs R -m $d
