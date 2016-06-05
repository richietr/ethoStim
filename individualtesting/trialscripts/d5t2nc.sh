export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Thu Jun 9 11:05:00 2016' +%s); python trial.py -f Harriet -ps 5.png -ts 10 -d 5 -s 2 -fs right -x female -p 50 -sp gambusia -sl 367 -r 1 -cs R -m $d
