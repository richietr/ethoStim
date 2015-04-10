

# imports
import sys
import time
import csv
from psychopy import visual, core, event
import os
import subprocess


# housekeeping
clock = core.Clock()
date = time.strftime('%m%d%Y')
now = time.strftime('%X')
nowfolder = time.strftime('%H%M%S')


# open output csv file for writing or appending
f = os.path.join(os.getcwd() + 'Data_' + date + '/' + date + '_ethotrials.csv')

try:
    fsize = os.stat(f).st_size
except OSError:
    w = csv.writer(open(f, 'w'), delimiter=',')
    w.writerow(
        ['date', 'trial time start', 'stimulus ID', 'trial type', 'fish group', 'stimulus1 name', 'stimulus1 screen',
         'stimulus2 name',
         'stimulus2 screen'])
else:
    if fsize > 0:
        w = csv.writer(open(f, 'a'), delimiter=',')
# fish specification
try:
    pesces = sys.argv[3]
except IndexError:
    print "you forgot to say which fish these are (e.g.; 'm1_f3' -[lftf_rghtf]"
    pesces = 'lf?rf?'

# presentation windows
win1 = visual.Window(screen=0, size=(1920, 1080), pos=(0, 0))
win2 = visual.Window(screen=1, size=(1920, 1080), pos=(0, 0))

# stimulus picking tree, adjust trial TypeIDs/stimulus combinations here
try:
    stimID = sys.argv[1]
    if stimID == '5_10':
        trialstim1 = visual.ImageStim(win1, image='5.png', pos=(0, 0.75), colorSpace='rgb', name='5.png')
        trialstim2 = visual.ImageStim(win2, image='10.png', pos=(0, 0.75), colorSpace='rgb', name='10.png')
    if stimID == '6_12':
        trialstim1 = visual.ImageStim(win1, image='6.png', pos=(0, 0.75), colorSpace='rgb', name='6.png')
        trialstim2 = visual.ImageStim(win2, image='12.png', pos=(0, 0.75), colorSpace='rgb', name='12.png')
    if stimID == '7_14':
        trialstim1 = visual.ImageStim(win1, image='7.png', pos=(0, 0.75), colorSpace='rgb', name='7.png')
        trialstim2 = visual.ImageStim(win2, image='14.png', pos=(0, 0.75), colorSpace='rgb', name='14.png')
    if stimID == '8_12':
        trialstim1 = visual.ImageStim(win1, image='8.png', pos=(0, 0.75), colorSpace='rgb', name='8.png')
        trialstim2 = visual.ImageStim(win2, image='12.png', pos=(0, 0.75), colorSpace='rgb', name='12.png')
    if stimID == '9_12':
        trialstim1 = visual.ImageStim(win1, image='9.png', pos=(0, 0.75), colorSpace='rgb', name='9.png')
        trialstim2 = visual.ImageStim(win2, image='12.png', pos=(0, 0.75), colorSpace='rgb', name='12.png')
    if stimID == 'acclim':
        trialstim1 = visual.ImageStim(win1, image='0.png', pos=(0, 0.75), colorSpace='rgb', name='0.png')
        trialstim2 = visual.ImageStim(win2, image='0.png', pos=(0, 0.75), colorSpace='rgb', name='0.png')
    if stimID == '10_5':
        trialstim1 = visual.ImageStim(win2, image='5.png', pos=(0, 0.75), colorSpace='rgb', name='5.png')
        trialstim2 = visual.ImageStim(win1, image='10.png', pos=(0, 0.75), colorSpace='rgb', name='10.png')
    if stimID == '12_6':
        trialstim1 = visual.ImageStim(win2, image='6.png', pos=(0, 0.75), colorSpace='rgb', name='6.png')
        trialstim2 = visual.ImageStim(win1, image='12.png', pos=(0, 0.75), colorSpace='rgb', name='12.png')
    if stimID == '14_7':
        trialstim1 = visual.ImageStim(win2, image='7.png', pos=(0, 0.75), colorSpace='rgb', name='7.png')
        trialstim2 = visual.ImageStim(win1, image='14.png', pos=(0, 0.75), colorSpace='rgb', name='14.png')
    if stimID == '12_8':
        trialstim1 = visual.ImageStim(win2, image='8.png', pos=(0, 0.75), colorSpace='rgb', name='8.png')
        trialstim2 = visual.ImageStim(win1, image='12.png', pos=(0, 0.75), colorSpace='rgb', name='12.png')
    if stimID == '12_9':
        trialstim1 = visual.ImageStim(win2, image='9.png', pos=(0, 0.75), colorSpace='rgb', name='9.png')
        trialstim2 = visual.ImageStim(win1, image='12.png', pos=(0, 0.75), colorSpace='rgb', name='12.png')

except IndexError:
    print "you forgot to say what trial type. defaulting to 'acclim'"
    trialstim1 = visual.ImageStim(win2, image='0.png', pos=(0, 0.75), colorSpace='rgb', name='9.png')
    trialstim2 = visual.ImageStim(win1, image='0.png', pos=(0, 0.75), colorSpace='rgb', name='9.png')


# training or probe trial/length
try:
    ttID = sys.argv[2]
    if ttID == 'train':
        tLength = 7 * 60
    if ttID == 'probe':
        tLength = 7 * 60
except IndexError:
    print "you forgot to say if this is a 'train' or 'probe' trial"
    tLength = 4 * 60

try:
    w.writerow([date, now, stimID, ttID, pesces, trialstim1.name, trialstim1.win.screen, trialstim2.name,
                trialstim2.win.screen])
except NameError:
    w.writerow([date, now, 'stimID missing', 'ttID missing', 'fishids missing', trialstim1.name, trialstim1.win.screen,
                trialstim2.name,
                trialstim2.win.screen])


allKeys = event.waitKeys()


# hang here until trial is started
for thisKey in allKeys:
    if thisKey == 's':


        # adjust these commands based on OS anddesired video format/codec. These capture Isight cam ('0') and desktop ('1') on OSX 10.10.2
        subprocess.Popen(['ffmpeg', '-f', 'avfoundation', '-i', '0', '-t', str(tLength / 60), '../out.mpg'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
        subprocess.Popen(['ffmpeg', '-f', 'avfoundation', '-i', '1', '-t', str(tLength / 60), '../out2.mpg'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)


        for FrameN in range(tLength):
            trialstim1.draw()
            trialstim2.draw()
            win1.flip()
            win2.flip()

exit()