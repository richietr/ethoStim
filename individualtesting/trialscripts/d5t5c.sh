export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Thu September 22 17:05:00 2016' +%s); python trial.py -f Lynn -ps 10.png -ts 5 -d 5 -s 5 -fs left -x female -p 50 -sp gambusia -sl TBD -r 6 -cs L -c -m $d
