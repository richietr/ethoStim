export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Wed August 10 17:05:00 2016' +%s); python trial.py -f Heidi -ps 10.png -ts 5 -d 3 -s 5 -fs left -x female -p 50 -sp gambusia -sl TBD -r 4 -cs L -fd -m $d
