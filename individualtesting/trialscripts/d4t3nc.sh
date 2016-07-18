export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue July 19 13:05:00 2016' +%s); python trial.py -f Harlow -ps 6.png -ts 12 -d 4 -s 3 -fs left -x female -p 50 -sp gambusia -sl 328 -r 3 -cs L -fd -m $d
