export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Wed June 29 15:05:00 2016' +%s); python trial.py -f Layla -ps 6.png -ts 12 -d 6 -s 4 -fs left -x female -p 50 -sp gambusia -sl 367 -r 1 -cs L -fd -m $d
