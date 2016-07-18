export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Fri July 22 9:05:00 2016' +%s); python trial.py -f Harlow -ps 10.png -ts 5 -d 7 -s 1 -fs left -x female -p 50 -sp gambusia -sl 328 -r 3 -cs L -c -m $d
