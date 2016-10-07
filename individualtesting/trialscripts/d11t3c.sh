export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Wed September 28 13:05:00 2016' +%s); python trial.py -f Lynn -ps 9.png -ts 12 -d 11 -s 3 -fs none -x female -p 75 -sp gambusia -sl TBD -r 6 -cs R -c -m $d
