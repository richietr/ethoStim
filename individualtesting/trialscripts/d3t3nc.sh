export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sun June 26 13:05:00 2016' +%s); python trial.py -f Layla -ps 12.png -ts 6 -d 3 -s 3 -fs right -x female -p 50 -sp gambusia -sl 367 -r 1 -cs R -m $d
