export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue September 27 9:05:00 2016' +%s); python trial.py -f Lynn -ps 9.png -ts 12 -d 10 -s 1 -fs none -x female -p 75 -sp gambusia -sl TBD -r 6 -cs R -c -m $d
