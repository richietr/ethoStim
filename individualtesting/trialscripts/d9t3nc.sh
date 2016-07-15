export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Fri July 22 13:05:00 2016' +%s); python trial.py -f Harlow -ps 14.png -ts 7 -d 9 -s 3 -fs none -x female -p 50 -sp gambusia -sl 328 -r 3 -cs R -m $d
