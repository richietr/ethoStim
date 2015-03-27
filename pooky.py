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
win1 = visual.Window(screen=0, size=(1920, 1080), pos=(0, 0))
win2 = visual.Window(screen=1, size=(1920, 1080), pos=(0, 0))


# list out all stimulus images here
stim5 = visual.ImageStim(win1, image='5.png', pos=(0, 0.75), colorSpace='rgb', name='5.png')
stim6 = visual.ImageStim(win2, image='6.png', pos=(0, 0.75), colorSpace='rgb', name='6.png')
stim7 = visual.ImageStim(win1, image='7.png', pos=(0, 0.75), colorSpace='rgb', name='7.png')
stim8 = visual.ImageStim(win2, image='8.png', pos=(0, 0.75), colorSpace='rgb', name='8.png')
stim9 = visual.ImageStim(win1, image='9.png', pos=(0, 0.75), colorSpace='rgb', name='9.png')
stim10 = visual.ImageStim(win2, image='10.png', pos=(0, 0.75), colorSpace='rgb', name='10.png')
stim12 = visual.ImageStim(win1, image='12.png', pos=(0, 0.75), colorSpace='rgb', name='12.png')
stim14 = visual.ImageStim(win2, image='14.png', pos=(0, 0.75), colorSpace='rgb', name='14.png')
stim0 = visual.ImageStim(win1, image='0.png', pos=(0, 0.75), colorSpace='rgb', name='0.png')
stim00 = visual.ImageStim(win2, image='0.png', pos=(0, 0.75), colorSpace='rgb', name='0.png')


# stimulus picking tree, adjust trial TypeIDs/stimulus combinations here
try:
    stimID = sys.argv[1]
    if stimID == '5_10':
        trialstim1 = stim5
        trialstim2 = stim10
    if stimID == '6_12':
        trialstim1 = stim6
        trialstim2 = stim12
    if stimID == '7_14':
        trialstim1 = stim7

        trialstim2 = stim14
    if stimID == '8_12':
        trialstim1 = stim8
        trialstim2 = stim12
    if stimID == '9_12':
        trialstim1 = stim9
        trialstim2 = stim12
    if stimID == 'acclim':
        trialstim1 = stim0
        trialstim2 = stim00
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


# alternate side stimulus is displayed on
csvf_length = sum(1 for row in f)

if csvf_length % 2 == 0:
    trialstim1.win = win2
    trialstim2.win = win1
else:
    trialstim1.win = win1
    trialstim2.win = win2


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


# do it
while cap.isOpened():
    for FrameN in range(tLength):

        ret2, frame2 = cap2.read()
        ret, frame = cap.read()


        fn = '%s/%03d.bmp' % (shotdir1, shot_idx)
        fn1 = '%s/%03d.bmp' % (shotdir2, shot_idx)
        cv2.imwrite(fn, frame)
        cv2.imwrite(fn1, frame2)
        if ord('q') == cv2.waitKey(1) & 0xFF:
            break

        display()
        shot_idx += 1
    cap.release()


try:
    w.writerow([date, now, stimID, ttID, pesces, trialstim1.name, trialstim1.win.screen, trialstim2.name, trialstim2.win.screen])
except NameError:
    w.writerow([date, now, 'stimID missing', 'ttID missing', 'fishids missing', trialstim1.name, trialstim1.win.screen, trialstim2.name,

                trialstim2.win.screen])


cv2.destroyAllWindows()