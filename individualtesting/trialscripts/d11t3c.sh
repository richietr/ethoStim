export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sun July 24 13:05:00 2016' +%s); python trial.py -f Harlow -ps 8.png -ts 12 -d 11 -s 3 -fs none -x female -p 67 -sp gambusia -sl 328 -r 3 -cs R -c -m $d
