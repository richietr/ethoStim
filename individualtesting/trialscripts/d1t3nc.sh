export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" May 18 13:05:00 2016' +%s); python trial.py -f Second -ps 5.png -ts 10 -d 1 -s 3 -fs right -x female -p 50 -sp gambusia -sl 367 -r 1 -m $d
