export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue July 26 16:05:00 2016' +%s); python trialblack.py -fd -m $d
