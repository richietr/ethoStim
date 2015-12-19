__author__ = 'RobertIan'
__version__ = '4.0.1'
'''
///////////////////////////////////////////////////////////
//  Permission is hereby granted, free of charge,
//  to any person obtaining a copy of
//  this software and associated documentation files
//  (the "Software"), to deal in the Software without
//  restriction, including without limitation the rights
//  to use, copy, modify, merge, publish, distribute,
//  sublicense, and/or sell copies of the Software, and
//  to permit persons to whom the Software is furnished
//  to do so, subject to the following conditions:
//
//  The above copyright notice and this permission notice
//  shall be included in all copies or substantial portions
//  of the Software.
//
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF
//  ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
//  TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
//  PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
//  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
//  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
//  OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
//  IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
//  DEALINGS IN THE SOFTWARE.
'''
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


    def __init__(self, date, now, day, session, leftFish, rightFish, highStim,
    lowStim, cond, roundd, sll, slr, sexl, sexr, species):
        self.lftpez = leftFish
        self.rgtpez = rightFish
        self.day = day
        self.session = session
        self.hstim = highStim
        self.lstim = lowStim
        self.conditionside = cond
        self.win1 = visual.Window(pos=[0.0,0.0], units='height',
        winType='pyglet', monitor=None, screen=1, size=[832.0,624.0])
        self.win2 = visual.Window(pos=[0.0,0.0], units='height',
        winType='pyglet', monitor=None, screen=2, size=[832.0,624.0])
        self.tLength = 4 * 60
        self.clock = core.Clock()
        self.lfi = leftFish[0] #this script assumes the naming convention that uses
        self.rfi = rightFish[0] # 'H' and 'L' as the first letter of IDs
        coni = cond[0] # assumer 'Right' or 'R' and 'Left' or 'L'
        self.round = roundd
        self.SLl = sll
        self.SLr = slr
        self.sexl = sexl
        self.sexr = sexr
        self.species = species



    def parseStimulus(self):

        # This is very clunky and non-Pythonic but it works...

        '''
        The idea is this:

        The Left tank's stimulus orientation determine the stimID
        The Right tank's stimulus are dependent and inverse
        SO:

        Left tank        Right tank
        |            |   |            |
        |            |   |            |
        |High     Low|___|Low     High|
        ______________   ______________

        would result in a stimID of 'int(High)_int(Low)'

                Left tank        Right tank
                |            |   |            |
                |            |   |            |
                |Low     High|___|High     Low|
                ______________   ______________

                would result in a stimID of 'int(Low)_int(High)'

        The individuals in each tank determine which side the reward condition
        will be presented (but these will always be the same side for both
        tanks in any given trial as long as a 'High' and 'Low' individual are
        always paired

        e.g.:

        Left tank        Right tank
        HIGH FISH        LOW FISH
        fed side (Left):
          |                |
          V                V
        |            |   |            |
        |            |   |            |
        |High     Low|___|Low     High|
        ______________   ______________

                Left tank        Right tank
                LOW FISH         HIGH FISH
                fed side (Right):
                           |                |
                           V                V
                |            |   |            |
                |            |   |            |
                |High     Low|___|Low     High|
                ______________   ______________

        the inverse is also possible as the 'High' and 'Low' sides are randomized
        '''
        lfi = self.lfi
        rfi = self.rfi

        self.lcondstim = (self.lstim if lfi == 'L' else self.hstim)
        self.rcondstim = (self.hstim if rfi == 'H' else self.lstim)

        print lfi, rfi, coni
        if lfi == 'H' and rfi == 'L' and coni == 'R':
            self.stimID = str(lowStim)+'_'+str(highStim)
        if lfi == 'H' and rfi == 'L' and coni == 'L':
            self.stimID = str(highStim)+'_'+str(lowStim)
        if lfi =='L' and rfi == 'H' and coni == 'R':
            self.stimID = str(highStim)+'_'+str(lowStim)
        if lfi =='L' and rfi == 'H' and coni == 'L':
            self.stimID = str(lowStim)+'_'+str(highStim)
        if lfi =='L' and rfi == 'H' and coni == 'b':
            self.stimID = str(lowStim)+'_'+str(highStim)
        if lfi =='H' and rfi == 'L' and coni == 'b':
            self.stimID = str(lowStim)+'_'+str(highStim)
        if lfi =='L' and rfi == 'H' and coni == 'n':
            self.stimID = str(lowStim)+'_'+str(highStim)
        if lfi =='H' and rfi == 'L' and coni == 'n':
            self.stimID = str(lowStim)+'_'+str(highStim)

        self.lftstim, self.rgtstim = self.stimID.split("_")

        try:
            if self.stimID == '5_10':
                self.trialstim1 = visual.ImageStim(win1, image='5.png',
                pos=(0, 0), colorSpace='rgb', name='5.png')
                self.trialstim2 = visual.ImageStim(win2, image='10.png',
                pos=(0, 0), colorSpace='rgb', name='10.png')
            if self.stimID == '6_12':
                self.trialstim1 = visual.ImageStim(win1, image='6.png',
                pos=(0, 0), colorSpace='rgb', name='6.png')
                self.trialstim2 = visual.ImageStim(win2, image='12.png',
                pos=(0, 0), colorSpace='rgb', name='12.png')
            if self.stimID == '7_14':
                self.trialstim1 = visual.ImageStim(win1, image='7.png',
                pos=(0, 0), colorSpace='rgb', name='7.png')
                self.trialstim2 = visual.ImageStim(win2, image='14.png',
                pos=(0, 0), colorSpace='rgb', name='14.png')
            if self.stimID == '8_12':
                self.trialstim1 = visual.ImageStim(win1, image='8.png',
                pos=(0, 0), colorSpace='rgb', name='8.png')
                self.trialstim2 = visual.ImageStim(win2, image='12.png',
                pos=(0, 0), colorSpace='rgb', name='12.png')
            if self.stimID == '9_12':
                self.trialstim1 = visual.ImageStim(win1, image='9.png',
                pos=(0, 0), colorSpace='rgb', name='9.png')
                self.trialstim2 = visual.ImageStim(win2, image='12.png',
                pos=(0, 0), colorSpace='rgb', name='12.png')
            if self.stimID == '0_0':
                self.trialstim1 = visual.ImageStim(win1, image='0.png',
                pos=(0, 0), colorSpace='rgb', name='0.png')
                self.trialstim2 = visual.ImageStim(win2, image='0.png',
                pos=(0, 0), colorSpace='rgb', name='0.png')
            if self.stimID == '10_5':
                self.trialstim1 = visual.ImageStim(win2, image='5.png',
                pos=(0, 0), colorSpace='rgb', name='5.png')
                self.trialstim2 = visual.ImageStim(win1, image='10.png',
                pos=(0, 0), colorSpace='rgb', name='10.png')
            if self.stimID == '12_6':
                self.trialstim1 = visual.ImageStim(win2, image='6.png',
                pos=(0, 0), colorSpace='rgb', name='6.png')
                self.trialstim2 = visual.ImageStim(win1, image='12.png',
                pos=(0, 0), colorSpace='rgb', name='12.png')
            if self.stimID == '14_7':
                self.trialstim1 = visual.ImageStim(win2, image='7.png',
                pos=(0, 0), colorSpace='rgb', name='7.png')
                self.trialstim2 = visual.ImageStim(win1, image='14.png',
                pos=(0, 0), colorSpace='rgb', name='14.png')
            if self.stimID == '12_8':
                self.trialstim1 = visual.ImageStim(win2, image='8.png',
                pos=(0, 0), colorSpace='rgb', name='8.png')
                self.trialstim2 = visual.ImageStim(win1, image='12.png',
                pos=(0, 0), colorSpace='rgb', name='12.png')
            if self.stimID == '12_9':
                self.trialstim1 = visual.ImageStim(win2, image='9.png',
                pos=(0, 0), colorSpace='rgb', name='9.png')
                self.trialstim2 = visual.ImageStim(win1, image='12.png',
                pos=(0, 0), colorSpace='rgb', name='12.png')

        except IndexError:
            print "you forgot to say what trial type. defaulting to 'acclim'"
            self.trialstim1 = visual.ImageStim(win2, image='0.png', pos=(0, 0),
            colorSpace='rgb', name='0.png')
            self.trialstim2 = visual.ImageStim(win1, image='0.png', pos=(0, 0),
            colorSpace='rgb', name='0.png')

    def randori(self):
        orifoo = [90, 180, 270, 0, 360]
        self.ori1 = int(random.choice(orifoo))
        self.ori2 = int(random.choice(orifoo))
        self.trialstim1.ori = self.ori1
        self.trialstim2.ori = self.ori2

    def filenames(self):
        # File names will be in this order: species, roundd, SL, sex, indnom,
        #day, session, stimulus, presside, tank
        self.leftvid = (str(self.species)+'_'+str(self.round)+'_'+str(self.SLl)+'_'+
        str(self.sexl) +'_'+str(self.lftpez)+'_'+str(self.day)+'_'+
        str(self.session)+'_' +str(self.lcondstim)+'_'+str(self.conditionside)+
        '_'+'LEFTTANK'+'.mpg')
        self.rightvid = (str(self.species)+'_'+str(self.round)+'_'+str(self.SLr)+'_'+
        str(self.sexr)+'_'+str(self.rgtpez)+'_'+str(self.day)+'_'+
        str(self.session)+'_'+str(self.rcondstim)+'_'+str(self.conditionside)+
        '_'+'RIGHTTANK'+'.mpg')

    def runtry(self):
        allKeys = event.waitKeys()
        for thisKey in allKeys:
            if thisKey == 's':
                # start cameras
                self.p1 = subprocess.Popen(
            ['ffmpeg', '-f', 'avfoundation', '-r', '20', '-s', '1920x1080',
            '-i', '2', '-t', str(self.tLength), str(self.leftvid)])

                self.p2 = subprocess.Popen(
            ['ffmpeg', '-f', 'avfoundation', '-r', '20', '-s', '1920x1080',
             '-i', '0', '-t', str(self.tLength), str(self.rightvid)])




                startT = self.clock.getTime()
                # present stimluls
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
                            self.p1.kill()
                            self.p2.kill()
                            self.win1.close()
                            self.win2.close()
                            sys.exit()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-lf","--leftFish", help="ID of fish in left tank")
    ap.add_argument("-rf", "--rightFish", help="ID of fish in right tank")
    ap.add_argument("-hs", "--highStim", help="high numerosity stimulus, e.g. 12")
    ap.add_argument("-ls", "--lowStim", help="low numerosity stimulus, e.g. 6")
    ap.add_argument("-d","--day", help="experiment day, e.g. 1-7")
    ap.add_argument("-s","--session", help="trial session, e.g. 1-4")
    ap.add_argument("-fs","--fedSide", help="side feed on/conditioned side")
    ap.add_argument("-x","--sex", help="trial day")
    ap.add_argument("-p","--ratio", help="trial day")
    ap.add_argument("-sp", "--species", help="species name")
    ap.add_argument("-fn", "--fishName", help="the name of the focal fish")
    ap.add_argument("-rsl","--rightfishstandardlength", help="the standard length of the fish in the right tank")
    ap.add_argument("-lsl","--leftfishstandardlength", help="the standard length of the fish in the left tank")
    ap.add_argument("-r","--round", help="the round of the trial")
    ap.add_argument("-st", "--stimulus", help="stimulus presented")
    ap.add_argument("-rfs", "--rightfishsex", help="sex of fish in right tank")
    ap.add_argument("-lfs", "--leftfishsex", help="sex of fish in right tank")

    args = vars(ap.parse_args())

    RT = Trial(time.strftime('%m%d%Y'), time.strftime('%X'), args["day"], args["session"],
    args["leftFish"], args["rightFish"], args["highStim"], args["lowStim"], args["fedSide"],
    args["round"], args["leftfishstandardlength"], args["rightfishstandardlength"],
    args["leftfishsex"], args["rightfishsex"], args["species"])
    RT.parseStimulus()
    RT.randori()
    RT.filenames()
    subprocess.Popen(["osascript", "screenset.scpt"])

    RT.runtry()

    core.quit()
    _exit()
