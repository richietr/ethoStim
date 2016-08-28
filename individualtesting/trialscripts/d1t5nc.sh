export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Mon August 8 17:05:00 2016' +%s); python trial.py -f Heidi -ps 0.png -ts 0 -d 1 -s 5 -fs both -x female -p 0 -sp gambusia -sl TBD -r 4 -cs B -fd -m $d
