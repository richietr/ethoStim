export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue September 20 15:05:00 2016' +%s); python trial.py -f Lynn -ps 5.png -ts 10 -d 3 -s 4 -fs left -x female -p 50 -sp gambusia -sl TBD -r 6 -cs L -fd -m $d
