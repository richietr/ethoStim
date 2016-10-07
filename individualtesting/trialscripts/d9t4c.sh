export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Mon September 26 15:05:00 2016' +%s); python trial.py -f Lynn -ps 12.png -ts 6 -d 9 -s 4 -fs left -x female -p 50 -sp gambusia -sl TBD -r 6 -cs L -c -m $d
