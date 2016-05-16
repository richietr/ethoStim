export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" May 24 15:05:00 2016' +%s); python trial.py -f Second -ps 0.png -ts 0 -d 7 -s 4 -fs both -x female -p 0 -sp gambusia -sl 367 -r 1 -fd -c -m $d
