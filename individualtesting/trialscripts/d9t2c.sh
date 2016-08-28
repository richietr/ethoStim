export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue August 16 11:05:00 2016' +%s); python trial.py -f Heidi -ps 12.png -ts 8 -d 9 -s 2 -fs none -x female -p 67 -sp gambusia -sl TBD -r 4 -cs R -c -m $d
