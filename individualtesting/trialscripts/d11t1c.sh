export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sun July 24 9:05:00 2016' +%s); python trial.py -f Harlow -ps 7.png -ts 14 -d 11 -s 1 -fs none -x female -p 50 -sp gambusia -sl 328 -r 3 -cs R -c -m $d
