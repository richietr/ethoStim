export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue August 16 9:05:00 2016' +%s); python trial.py -f Heidi -ps 9.png -ts 12 -d 9 -s 1 -fs none -x female -p 75 -sp gambusia -sl TBD -r 4 -cs L -c -m $d
