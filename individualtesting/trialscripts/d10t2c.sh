export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Wed August 17 11:05:00 2016' +%s); python trial.py -f Heidi -ps 14.png -ts 7 -d 10 -s 2 -fs none -x female -p 50 -sp gambusia -sl TBD -r 4 -cs R -c -m $d
