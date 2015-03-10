# imports
import sys
from psychopy import visual, core


# housekeeping
clock = core.Clock()


# presentation windows
win1 = visual.Window(screen=0, size=(1920, 1080), pos=(0, 0))
win2 = visual.Window(screen=1, size=(1920, 1080), pos=(0, 0))


# list out all stimulus images here
stim1 = visual.ImageStim(win1, image='5.png', pos=(0, 0.75), colorSpace='rgb')
stim2 = visual.ImageStim(win2, image='6.png', pos=(0, 0.75), colorSpace='rgb')
stim3 = visual.ImageStim(win1, image='7.png', pos=(0, 0.75), colorSpace='rgb')
stim4 = visual.ImageStim(win2, image='8.png', pos=(0, 0.75), colorSpace='rgb')
stim5 = visual.ImageStim(win1, image='9.png', pos=(0, 0.75), colorSpace='rgb')
stim6 = visual.ImageStim(win2, image='10.png', pos=(0, 0.75), colorSpace='rgb')
stim7 = visual.ImageStim(win1, image='12.png', pos=(0, 0.75), colorSpace='rgb')
stim8 = visual.ImageStim(win2, image='14.png', pos=(0, 0.75), colorSpace='rgb')
stim9 = visual.ImageStim(win1, image='0.png', pos=(0, 0.75), colorSpace='rgb')
stim10 = visual.ImageStim(win2, image='0.png', pos=(0, 0.75), colorSpace='rgb')

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



