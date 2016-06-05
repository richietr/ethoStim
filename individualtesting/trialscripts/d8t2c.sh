export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sun Jun 12 11:05:00 2016' +%s); python trial.py -f Harriet -ps 12.png -ts 9 -d 8 -s 2 -fs none -x female -p 75 -sp gambusia -sl 367 -r 1 -cs R -c -m $d
