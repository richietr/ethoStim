export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Mon September 26 9:05:00 2016' +%s); python trial.py -f Lynn -ps 7.png -ts 14 -d 9 -s 1 -fs none -x female -p 50 -sp gambusia -sl TBD -r 6 -cs R -c -m $d
