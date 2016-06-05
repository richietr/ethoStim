export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sat Jun 11 13:05:00 2016' +%s); python trial.py -f Harriet -ps 12.png -ts 9 -d 7 -s 3 -fs none -x female -p 75 -sp gambusia -sl 367 -r 1 -cs L -m $d
