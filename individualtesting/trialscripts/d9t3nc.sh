export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue August 16 13:05:00 2016' +%s); python trial.py -f Heidi -ps 14.png -ts 7 -d 9 -s 3 -fs none -x female -p 50 -sp gambusia -sl TBD -r 4 -cs L -m $d
