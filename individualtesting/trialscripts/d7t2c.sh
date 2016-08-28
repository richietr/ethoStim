export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sun August 14 11:05:00 2016' +%s); python trial.py -f Heidi -ps 6.png -ts 12 -d 7 -s 2 -fs left -x female -p 50 -sp gambusia -sl TBD -r 4 -cs L -c -m $d
