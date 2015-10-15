__author__ = 'ian'


# imports
import sys
import time
import csv
from psychopy import visual, core, event, monitors
import os
import subprocess
import random
import argparse


class Trial:


    def __init__(self, date, now, day, session, leftFish, rightFish, highStim, lowStim, cond):
        self.lftpez = leftFish
        self.rgtpez = rightFish
        self.day = day
        self.session = session
        self.hstim = highStim
        self.lstim = lowStim
        self.conditionside = cond
        win1 = visual.Window(pos=[0.0,0.0], units='height', winType='pyglet', monitor=None, screen=1, size=[832.0,624.0])
        win2 = visual.Window(pos=[0.0,0.0], units='height', winType='pyglet', monitor=None, screen=2, size=[832.0,624.0])
        self.win1 = win1
        self.win2 = win2
        self.tLength = 4 * 60
        self.clock = core.Clock()
        lfi = leftFish[0]
        rfi = rightFish[0]
        coni = cond[0]

        print lfi, rfi, coni
        if lfi == 'H' and rfi == 'L' and coni == 'R':
            self.stimID = str(highStim)+'_'+str(lowStim)
        if lfi == 'H' and rfi == 'L' and coni == 'L':
            self.stimID = str(lowStim)+'_'+str(highStim)
        if lfi =='L' and rfi == 'H' and coni == 'R':
            self.stimID = str(lowStim)+'_'+str(highStim)
        if lfi =='L' and rfi == 'H' and coni == 'L':
            self.stimID = str(highStim)+'_'+str(lowStim)
        if lfi =='L' and rfi == 'H' and coni == 'b':
            self.stimID = str(highStim)+'_'+str(lowStim)
        if lfi =='H' and rfi == 'L' and coni == 'b':
            self.stimID = str(highStim)+'_'+str(lowStim)
        if lfi =='L' and rfi == 'H' and coni == 'n':
            self.stimID = str(highStim)+'_'+str(lowStim)
        if lfi =='H' and rfi == 'L' and coni == 'n':
            self.stimID = str(highStim)+'_'+str(lowStim)
        '''
        f = os.path.join(os.getcwd() + date + '_ethotrials.csv')
        try:
            fsize = os.stat(f).st_size
        except OSError:
            self.w = csv.writer(open(f, 'r+w+'))
            self.w.writerow(
                ['date', 'start time', 'day', 'trial session', 'left fish', 'right fish',
                 'high stim','lowstim','side fed'])
        else:
            if fsize > 0:
                self.w = csv.writer(open(f, 'a+'), delimiter=',')
                '''
        try:

            if self.stimID == '5_10':
                self.trialstim1 = visual.ImageStim(win1, image='5.png', pos=(0, 0), colorSpace='rgb', name='5.png')
                self.trialstim2 = visual.ImageStim(win2, image='10.png', pos=(0, 0), colorSpace='rgb', name='10.png')
            if self.stimID == '6_12':
                self.trialstim1 = visual.ImageStim(win1, image='6.png', pos=(0, 0), colorSpace='rgb', name='6.png')
                self.trialstim2 = visual.ImageStim(win2, image='12.png', pos=(0, 0), colorSpace='rgb', name='12.png')
            if self.stimID == '7_14':
                self.trialstim1 = visual.ImageStim(win1, image='7.png', pos=(0, 0), colorSpace='rgb', name='7.png')
                self.trialstim2 = visual.ImageStim(win2, image='14.png', pos=(0, 0), colorSpace='rgb', name='14.png')
            if self.stimID == '8_12':
                self.trialstim1 = visual.ImageStim(win1, image='8.png', pos=(0, 0), colorSpace='rgb', name='8.png')
                self.trialstim2 = visual.ImageStim(win2, image='12.png', pos=(0, 0), colorSpace='rgb', name='12.png')
            if self.stimID == '9_12':
                self.trialstim1 = visual.ImageStim(win1, image='9.png', pos=(0, 0), colorSpace='rgb', name='9.png')
                self.trialstim2 = visual.ImageStim(win2, image='12.png', pos=(0, 0), colorSpace='rgb', name='12.png')
            if self.stimID == '0_0':
                self.trialstim1 = visual.ImageStim(win1, image='0.png', pos=(0, 0), colorSpace='rgb', name='0.png')
                self.trialstim2 = visual.ImageStim(win2, image='0.png', pos=(0, 0), colorSpace='rgb', name='0.png')
            if self.stimID == '10_5':
                self.trialstim1 = visual.ImageStim(win2, image='5.png', pos=(0, 0), colorSpace='rgb', name='5.png')
                self.trialstim2 = visual.ImageStim(win1, image='10.png', pos=(0, 0), colorSpace='rgb', name='10.png')
            if self.stimID == '12_6':
                self.trialstim1 = visual.ImageStim(win2, image='6.png', pos=(0, 0), colorSpace='rgb', name='6.png')
                self.trialstim2 = visual.ImageStim(win1, image='12.png', pos=(0, 0), colorSpace='rgb', name='12.png')
            if self.stimID == '14_7':
                self.trialstim1 = visual.ImageStim(win2, image='7.png', pos=(0, 0), colorSpace='rgb', name='7.png')
                self.trialstim2 = visual.ImageStim(win1, image='14.png', pos=(0, 0), colorSpace='rgb', name='14.png')
            if self.stimID == '12_8':
                self.trialstim1 = visual.ImageStim(win2, image='8.png', pos=(0, 0), colorSpace='rgb', name='8.png')
                self.trialstim2 = visual.ImageStim(win1, image='12.png', pos=(0, 0), colorSpace='rgb', name='12.png')
            if self.stimID == '12_9':
                self.trialstim1 = visual.ImageStim(win2, image='9.png', pos=(0, 0), colorSpace='rgb', name='9.png')
                self.trialstim2 = visual.ImageStim(win1, image='12.png', pos=(0, 0), colorSpace='rgb', name='12.png')



        except IndexError:
            print "you forgot to say what trial type. defaulting to 'acclim'"
            self.trialstim1 = visual.ImageStim(win2, image='0.png', pos=(0, 0), colorSpace='rgb', name='0.png')
            self.trialstim2 = visual.ImageStim(win1, image='0.png', pos=(0, 0), colorSpace='rgb', name='0.png')

    '''
    def writedat(self, date, now):

        self.w.writerow([date, now, self.day, self.session, self.lftpez, self.rgtpez, self.hstim, self.lstim,
                    self.conditionside])
'''
    def randori(self):
        orifoo = [90, 180, 270, 0, 360]
        self.ori1 = int(random.choice(orifoo))
        self.ori2 = int(random.choice(orifoo))
        self.trialstim1.ori = self.ori1
        self.trialstim2.ori = self.ori2


    def runtry(self):
        allKeys = event.waitKeys()
        for thisKey in allKeys:
            if thisKey == 's':
                self.p1 = subprocess.Popen(
            ['ffmpeg', '-f', 'avfoundation', '-r', '20', '-s', '1920x1080', '-i', '2', '-t', str(self.tLength),
             str(self.lftpez)+'_'+str(self.day)+'_'+str(self.session)+'.mpg'])

                self.p2 = subprocess.Popen(
            ['ffmpeg', '-f', 'avfoundation', '-r', '20', '-s', '1920x1080', '-i', '0', '-t', str(self.tLength),
             str(self.rgtpez)+'_'+str(self.day)+'_'+str(self.session)+'.mpg'])


                startT = self.clock.getTime()
                while (self.clock.getTime() - startT) < self.tLength:
            

                    restKeys = event.getKeys()
                    self.trialstim1.draw()
                    self.trialstim2.draw()
                    self.win1.flip()
                    self.win2.flip()
                    for thatKey in restKeys:
                        if thatKey == 'q':

                            print'exiting'
                            self.p1.communicate(input='q')
                            self.p2.communicate(input='q')
                            _exit()
                            self.p1.kill()
                            self.p2.kill()
                            # self.w.close()
                            self.win1.close()
                            self.win2.close()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-lf","--leftFish", help="ID of fish in left tank")
    ap.add_argument("-rf", "--rightFish", help="ID of fish in right tank")
    ap.add_argument("-hs", "--highStim", help="high numerosity stimulus, e.g. 12")
    ap.add_argument("-ls", "--lowStim", help="low numerosity stimulus, e.g. 6")
    ap.add_argument("-d","--day", help="experiment day, e.g. 1-7")
    ap.add_argument("-s","--session", help="trial session, e.g. 1-4")
    ap.add_argument("-fs","--fedSide", help="side feed on/conditioned side")
    args = vars(ap.parse_args())
    RT = Trial(time.strftime('%m%d%Y'), time.strftime('%X'), args["day"], args["session"], args["leftFish"],
               args["rightFish"], args["highStim"], args["lowStim"], args["fedSide"])
    RT.randori()
    #RT.writedat(time.strftime('%m%d%Y'), time.strftime('%X'))
    while 1:

        subprocess.Popen(["osascript", "screenset.scpt"])

        RT.runtry()

        core.quit()
        _exit()
