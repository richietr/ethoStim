export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Sat June 25 9:05:00 2016' +%s); python trial.py -f Layla -ps 0.png -ts 0 -d 2 -s 1 -fs both -x female -p 0 -sp gambusia -sl 367 -r 1 -cs B -fd -m $d
