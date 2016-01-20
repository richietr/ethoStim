#! /usr/python

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

__author__ = 'RobertIan'
__version__ = '0.1.1'

import argparse
import pygame
import picamera
import time
import netifaces
import RPi.GPIO as GPIO
import os.path

class Trial:

    def __init__(self, stim):
        # perhaps replace this with a bash script or RPC that controlls timing
        # of all servers
        #self.now = time.asctime()
        #self.when = when
        #assert self.when - self.now > 0
        #
        pygame.display.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.stimulus = stim
        #
        self.tLength = 4 * 60 #four minute trial
        self.feedDelay = 30 #thirty seconds
        #
        GPIO.setmode(GPIO.BCM)
        self.feeder = 5 ##
        self.notfeeder = 17 ##
        GPIO.setup(self.feeder, GPIO.OUT)
        GPIO.setup(self.notfeeder, GPIO.OUT)
        #
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1920, 1080)
        self.camera.framerate = 30
        self.cmera.autofocus = False
        self.camera.awb_mode = 'flourescent'
        startT = time.asctime()
        presented = False

    def checkPiIP(self):
        netifaces.ifaddresses('eth0')
        self.ip = ni.ifaddresses('eth0')[2][0]['addr']

    def whatStimulus(self):
        extension = os.path.splitext(self.stimulus)[1]
        if extension == '.png' or extension == '.PNG' or extension == '.jpg' \
        or extension == '.JPG':
        # still image
            try:
                self.image = pygame.image.load('src/',self.stimulus)
            except IOError:
                # currently a print, should be changed to send a message to
                #the client
                print 'are you sure this file exists? check the src folder \
                ony jpg/JPG, png/PNG formats'

        '''
        elif extension == '.mpg' or extension == '.MPG' or extension == '.avi' \
        or extension == '.AVI':
            try:
                self.video = pygame.image.load('src/',self.stimulus)
            except IOError:
                # currently a print should be changed to send a message to
                #the client
                print 'are you sure this file exists? check the src folder \
                ony jpg/JPG, ong/PNG, avi/AVI and mpg/MPG formats'
        '''
    def feed(self):
        GPIO.output(self.feeder, GPIO.HIGH)

    def notFeed(self):
        GPIO.output(self.notfeeder, GPIO.HIGH)

    def videoFileName(self, species, tround, sl, sex, fishid, day, session,
                    stim, conditionside):
        self.vidout = ('../data/',str(self.ip),'/',(str(species)+'_'+str(tround)
        +'_'+str(sl)+'_'+str(sex) +'_'+str(fishid)+'_'+str(day)+'_'+
        str(session)+'_' +str(stim)+'_'+str(conditionside)))

    def startRecording(self):
        self.camera.start_recording('%s.%s' % (str(self.vidout), 'mkv'))

    def stopRecording(self):
        self.camera.stop_recording()

    def safeQuit(self):
        GPIO.cleanup()
        pygame.quit()
        self.camera.close()
        exit()

    def mainLoop(self, feedornot):
        while (time.asctime() - startT) < self.tLength:

            try:
                delaymet = False
                if presented:
                    pass
                elif (time.asctime() - startT) < self.feedDelay:
                    delaymet = True
                if delaymet:
                    if
                self.screen.blit(self.image, (0,0))
                pygame.display.flip()
            except KeyboardInterrupt:
                self.safeQuit()




if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-f","--fish", help="ID of fish in tank")
    ap.add_argument("-ts", "--trainedStim",
        help="numerosity stimulus the individual is being trained to, e.g. 12")
    ap.add_argument("-ps", "--presentedStim", h
        help="stimulus being presented with this raspberry pi")
    ap.add_argument("-d","--day", help="experiment day, e.g. 1-7")
    ap.add_argument("-s","--session", help="trial session, e.g. 1-4")
    ap.add_argument("-fs","--fedSide", help="side feed on/conditioned side")
    ap.add_argument("-x","--sex", help="fish sex")
    ap.add_argument("-p","--ratio", help="training ratio")
    ap.add_argument("-sp", "--species", help="species name")
    ap.add_argument("-sl","--fishstandardlength", help="standard length of the")
    ap.add_argument("-r","--round", help="training round")
    ap.add_argument("-f", "--feed", help="feed with this stimulus",
                    action="store_true")
    ap.add_argument("-c", "--camera",
                    help="do you want to record using this pi?",
                    action="store_true")

    args = vars(ap.parse_args())

    T = Trial(args["presentedStim"])

    T.videoFileName(args["species"], args["round"], args["fishstandardlength"],
                    args["sex"], args["fish"], args["day"], args["session"],
                    args["trainedStim"], args["fedside"])
    T.checkPiIP()
    T.whatStimulus()
    if args["camera"]:
        T.startRecording()
    else:
        pass
    if args["feed"]:
        T.mainLoop(True)
    else:
        T.mainLoop(False)
    if args["camera"]:
        T.stoprecording()
    else:
        pass
    T.safeQuit()
