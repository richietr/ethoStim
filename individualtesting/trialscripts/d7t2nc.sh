export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sat Jun 11 11:05:00 2016' +%s); python trial.py -f Harriet -ps 7.png -ts 14 -d 7 -s 2 -fs none -x female -p 50 -sp gambusia -sl 367 -r 1 -cs R -m $d
