export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sat July 2 9:05:00 2016' +%s); python trial.py -f Layla -ps 14.png -ts 7 -d 9 -s 1 -fs none -x female -p 50 -sp gambusia -sl 367 -r 1 -cs R -m $d
