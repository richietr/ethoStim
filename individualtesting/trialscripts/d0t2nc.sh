export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" May 17 11:05:00 2016' +%s); python trial.py -f Second -ps 0.png -ts 0 -d 0 -s 2 -fs both -x female -p 0 -sp gambusia -sl 367 -r 1 -fd -m $d
