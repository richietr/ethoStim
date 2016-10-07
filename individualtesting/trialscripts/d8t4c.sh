export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sun September 25 15:05:00 2016' +%s); python trial.py -f Lynn -ps 5.png -ts 10 -d 8 -s 4 -fs right -x female -p 50 -sp gambusia -sl TBD -r 6 -cs R -fd -c -m $d
