export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Thu July 15 11:05:00 2016' +%s); python trial.py -f Harlow -ps 0.png -ts 0 -d 2 -s 2 -fs both -x female -p 0 -sp gambusia -sl 328 -r 3 -cs B -fd -m $d
