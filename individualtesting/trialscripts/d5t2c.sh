export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" May 22 11:05:00 2016' +%s); python trial.py -f Second -ps 14.png -ts 7 -d 5 -s 2 -fs none -x female -p 50 -sp gambusia -sl 367 -r 1 -c -m $d
