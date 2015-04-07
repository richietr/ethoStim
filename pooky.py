__author__ = 'ian'


# imports
import sys
import time
import csv
from psychopy import visual, core
import os
import cv2

# housekeeping
clock = core.Clock()
date = time.strftime('%m%d%Y')
now = time.strftime('%X')
nowfolder = time.strftime('%H%M%S')
shotdir1 = os.path.join(os.getcwd()+'Data_'+date+'/'+nowfolder+'/CAM1')
shotdir2 = os.path.join(os.getcwd()+'Data_'+date+'/'+nowfolder+'/CAM2')
os.makedirs(shotdir1)
os.makedirs(shotdir2)
shot_idx = 0


# open output csv file for writing or appending
f = os.path.join(os.getcwd()+'Data_'+date+'/'+date + '_ethotrials.csv')

try:
    fsize = os.stat(f).st_size
except OSError:
    w = csv.writer(open(f, 'w'), delimiter=',')
    w.writerow(['date', 'trial time start', 'stimulus ID', 'trial type', 'fish group',  'stimulus1 name', 'stimulus1 screen', 'stimulus2 name',
                'stimulus2 screen'])
else:
    if fsize > 0:
        w = csv.writer(open(f, 'a'), delimiter=',')
#fish specification
try:
    pesces = sys.argv[3]
except IndexError:
    print "you forgot to say which fish these are (e.g.; 'm1_f3' -[lftf_rghtf]"
    pesces = 'lf?rf?'

# presentation windows
win1 = visual.Window(screen=0, size=(1920, 1080), pos=(0, 0)) # need to adjust these for your displays
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
    trialstim1 = stim0
    trialstim2 = stim00


# training or probe trial/length
try:
    ttID = sys.argv[2]
    if ttID == 'train':
        tLength = 7 * 60 * 60
    if ttID == 'probe':
        tLength = 7 * 60 * 60
except IndexError:
    print "you forgot to say if this is a 'train' or 'probe' trial"
    tLength = 7 * 60


#blit displays
def display():
    trialstim1.draw()
    trialstim2.draw()
    win1.flip()
    win2.flip()

# set up captures
cap = cv2.VideoCapture(0)
width = cap.get(3)
height = cap.get(4)

cap2 = cv2.VideoCapture(1)
width2 = cap2.get(3)
height2 = cap2.get(4)

try:
    w.writerow([date, now, stimID, ttID, pesces, trialstim1.name, trialstim1.win.screen, trialstim2.name, trialstim2.win.screen])
except NameError:
    w.writerow([date, now, 'stimID missing', 'ttID missing', 'fishids missing', trialstim1.name, trialstim1.win.screen, trialstim2.name,

                trialstim2.win.screen])

# do it
while True:
    #for FrameN in range(tLength):
    ch = 0xFF & cv2.waitKey(1)
    if ch == ord('q'):
        break
    ret2, frame2 = cap2.read()
    ret, frame = cap.read()

    fn = '%s/%07d.png' % (shotdir1, shot_idx)
    fn1 = '%s/%07d.png' % (shotdir2, shot_idx)
    cv2.imwrite(fn, frame)
    cv2.imwrite(fn1, frame2)
    display()
    shot_idx += 1



cap.release()
cv2.destroyAllWindows()