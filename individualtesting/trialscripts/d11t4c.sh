export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue July 26 15:05:00 2016' +%s); python trial.py -f Harlow -ps 12.png -ts 6 -d 11 -s 4 -fs left -x female -p 50 -sp gambusia -sl 328 -r 3 -cs L -fd -c -m $d
