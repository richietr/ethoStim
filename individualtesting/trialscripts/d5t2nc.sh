export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Mon July 18 11:05:00 2016' +%s); python trial.py -f Harlow -ps 5.png -ts 10 -d 5 -s 2 -fs left -x female -p 50 -sp gambusia -sl 328 -r 3 -cs L -fd -m $d
