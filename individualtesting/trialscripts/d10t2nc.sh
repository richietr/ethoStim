export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue September 27 11:05:00 2016' +%s); python trial.py -f Lynn -ps 8.png -ts 12 -d 10 -s 2 -fs none -x female -p 67 -sp gambusia -sl TBD -r 6 -cs L -m $d
