export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Fri July 22 9:05:00 2016' +%s); python trial.py -f Harlow -ps 9.png -ts 12 -d 9 -s 1 -fs none -x female -p 75 -sp gambusia -sl 328 -r 3 -cs R -c -m $d
