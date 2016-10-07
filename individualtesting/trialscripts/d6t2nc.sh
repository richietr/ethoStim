export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Fri September 23 11:05:00 2016' +%s); python trial.py -f Lynn -ps 6.png -ts 12 -d 6 -s 2 -fs left -x female -p 50 -sp gambusia -sl TBD -r 6 -cs L -fd -m $d
