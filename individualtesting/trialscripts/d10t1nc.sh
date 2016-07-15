export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sat July 23 9:05:00 2016' +%s); python trial.py -f Harlow -ps 12.png -ts 8 -d 10 -s 1 -fs none -x female -p 67 -sp gambusia -sl 328 -r 3 -cs R -m $d
