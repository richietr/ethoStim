export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Fri Jun 10 9:05:00 2016' +%s); python trial.py -f Harriet -ps 10.png -ts 5 -d 6 -s 1 -fs left -x female -p 50 -sp gambusia -sl 367 -r 1 -cs L -fd -m $d
