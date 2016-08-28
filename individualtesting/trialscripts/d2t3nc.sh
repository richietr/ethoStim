export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue August 9 13:05:00 2016' +%s); python trial.py -f Heidi -ps 0.png -ts 0 -d 2 -s 3 -fs both -x female -p 0 -sp gambusia -sl TBD -r 4 -cs B -fd -m $d
