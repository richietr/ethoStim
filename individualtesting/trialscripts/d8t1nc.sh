export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sun Jun 12 9:05:00 2016' +%s); python trial.py -f Harriet -ps 14.png -ts 7 -d 8 -s 1 -fs none -x female -p 50 -sp gambusia -sl 367 -r 1 -cs L -m $d
