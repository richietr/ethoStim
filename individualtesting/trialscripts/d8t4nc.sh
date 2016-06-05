export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sun Jun 12 15:05:00 2016' +%s); python trial.py -f Harriet -ps 6.png -ts 12 -d 8 -s 4 -fs right -x female -p 50 -sp gambusia -sl 367 -r 1 -cs R -m $d
