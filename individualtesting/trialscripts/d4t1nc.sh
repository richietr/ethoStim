export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" May 21 9:05:00 2016' +%s); python trial.py -f Second -ps 12.png -ts 6 -d 4 -s 1 -fs left -x female -p 50 -sp gambusia -sl 367 -r 1 -fd -m $d
