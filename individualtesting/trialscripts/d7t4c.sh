export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sat Jun 11 15:05:00 2016' +%s); python trial.py -f Harriet -ps 10.png -ts 5 -d 7 -s 4 -fs right -x female -p 50 -sp gambusia -sl 367 -r 1 -cs R -fd -c -m $d
