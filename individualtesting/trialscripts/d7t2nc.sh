export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Thu June 30 11:05:00 2016' +%s); python trial.py -f Layla -ps 12.png -ts 6 -d 7 -s 2 -fs right -x female -p 50 -sp gambusia -sl 367 -r 1 -cs R -m $d
