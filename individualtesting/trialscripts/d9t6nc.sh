export DISPLAY=:0.0
cd /home/pi/ethoStim/individualtesting
d=$(date --date='TZ="US/Central" Tue August 16 16:10:00 2016' +%s); python trialblack.py -fd -m $d
