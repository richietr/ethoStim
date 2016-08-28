export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Wed August 17 9:05:00 2016' +%s); python trial.py -f Heidi -ps 8.png -ts 12 -d 10 -s 1 -fs none -x female -p 67 -sp gambusia -sl TBD -r 4 -cs L -c -m $d
