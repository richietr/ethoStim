export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Mon June 27 11:05:00 2016' +%s); python trial.py -f Layla -ps 10.png -ts 5 -d 4 -s 2 -fs right -x female -p 50 -sp gambusia -sl 367 -r 1 -cs R -m $d
