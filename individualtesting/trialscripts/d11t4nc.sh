export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Thu August 18 15:05:00 2016' +%s); python trial.py -f Heidi -ps 6.png -ts 12 -d 11 -s 4 -fs right -x female -p 50 -sp gambusia -sl TBD -r 4 -cs R -m $d
