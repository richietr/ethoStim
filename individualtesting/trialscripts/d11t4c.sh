export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Mon July 4 15:05:00 2016' +%s); python trial.py -f Layla -ps 10.png -ts 5 -d 11 -s 4 -fs left -x female -p 50 -sp gambusia -sl 367 -r 1 -cs L -fd -c -m $d
