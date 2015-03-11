# imports
import sys
import time
import os
import csv
from psychopy import visual, core

# housekeeping
clock = core.Clock()
date = time.strftime('%m%d%Y')
now = time.strftime('%X')

#open output csv file for writing or appending
f = date+'_ethotrials.csv'
try:
    fsize = os.stat(f).st_size 
except OSError:
    w = csv.writer(open(f, 'w'), delimiter=',')
    w.writerow(['date','trial time start','trial length','stimulus ID','trial type','win1 screen image','win2 screen image'])
else:
    if fsize > 0:
        w = csv.writer(open(f, 'a'), delimiter=',')

# presentation windows
win1 = visual.Window(screen=0, size=(1920, 1080), pos=(0, 0))
win2 = visual.Window(screen=1, size=(1920, 1080), pos=(0, 0))

# list out all stimulus images here
stim1 = visual.ImageStim(win1, image='5.png', pos=(0, 0.75), colorSpace='rgb', name='5.png')
stim2 = visual.ImageStim(win2, image='6.png', pos=(0, 0.75), colorSpace='rgb', name='6.png')
stim3 = visual.ImageStim(win1, image='7.png', pos=(0, 0.75), colorSpace='rgb', name='7.png')
stim4 = visual.ImageStim(win2, image='8.png', pos=(0, 0.75), colorSpace='rgb', name='8.png')
stim5 = visual.ImageStim(win1, image='9.png', pos=(0, 0.75), colorSpace='rgb', name='9.png')
stim6 = visual.ImageStim(win2, image='10.png', pos=(0, 0.75), colorSpace='rgb', name='10.png')
stim7 = visual.ImageStim(win1, image='12.png', pos=(0, 0.75), colorSpace='rgb', name='11.png')
stim8 = visual.ImageStim(win2, image='14.png', pos=(0, 0.75), colorSpace='rgb', name='12.png')
stim9 = visual.ImageStim(win1, image='0.png', pos=(0, 0.75), colorSpace='rgb', name='13.png')
stim10 = visual.ImageStim(win2, image='0.png', pos=(0, 0.75), colorSpace='rgb', name='14.png')

# stimulus picking tree, adjust trial TypeIDs/stimulus combinations here
try:
    stimID = sys.argv[1]
    if stimID == 'alpha':
        trialstim1 = stim1
        trialstim2 = stim6
    if stimID == 'beta':
        trialstim1 = stim2
        trialstim2 = stim7
    if stimID == 'gamma':
        trialstim1 = stim3

        trialstim2 = stim8
    if stimID == 'delta':
        trialstim1 = stim4
        trialstim2 = stim7
    if stimID == 'epsilon':
        trialstim1 = stim5
        trialstim2 = stim7
    if stimID == 'familiarization':
        trialstim1 = stim9
        trialstim2 = stim10
except IndexError:
    print "you forgot to say what trial type. defaulting to 'alpha'"
    trialstim1 = stim1
    trialstim2 = stim2

# training or probe trial/length
try:
    ttID = sys.argv[2]
    if ttID == 'train':
        tLength = 700
    if ttID == 'probe':
        tLength = 400
except IndexError:
    print "you forgot to say if this is a 'train' or 'probe' trial"
    tLength = 10

# run trial
for FrameN in range(tLength):
    trialstim1.draw()
    trialstim2.draw()
    win1.flip()
    win2.flip()

w.writerow([date,now,clock.getTime(),stimID,ttID,trialstim1.name,trialstim2.name])



