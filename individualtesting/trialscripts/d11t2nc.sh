export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Wed September 28 11:05:00 2016' +%s); python trial.py -f Lynn -ps 7.png -ts 14 -d 11 -s 2 -fs none -x female -p 50 -sp gambusia -sl TBD -r 6 -cs L -m $d
