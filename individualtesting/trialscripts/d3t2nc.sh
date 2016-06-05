export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue Jun 7 11:05:00 2016' +%s); python trial.py -f Harriet -ps 12.png -ts 6 -d 3 -s 2 -fs left -x female -p 50 -sp gambusia -sl 367 -r 1 -cs L -fd -m $d
