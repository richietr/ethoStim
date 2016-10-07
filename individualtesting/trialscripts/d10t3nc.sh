export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue September 27 13:05:00 2016' +%s); python trial.py -f Lynn -ps 14.png -ts 7 -d 10 -s 3 -fs none -x female -p 50 -sp gambusia -sl TBD -r 6 -cs R -m $d
