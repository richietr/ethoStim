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

__author__ = 'kjw2539'
__version__ = '0.1.1'

import argparse
import pygame
import picamera
import time
import datetime
import netifaces

import RPi.GPIO as GPIO
import os.path


#KJW imports
import sys
import select
import os

class Trial:

    def __init__(self, starttime):
        
        self.start = float(starttime)
        self.tLength = 45
      
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.cleanup()
        self.feeder = 17 ##
        self.notfeeder = 5 ##
      #GPIO.setup(27, GPIO.IN)
      #GPIO.add_event_detect(27, GPIO.RISING)
        GPIO.setup(self.feeder, GPIO.OUT)
        GPIO.output(self.feeder, True)
        GPIO.setup(self.notfeeder, GPIO.OUT)
        GPIO.output(self.notfeeder, False)
        print "GPIOinit"
#        self.camera = picamera.PiCamera()
#        self.camera.resolution = (1920, 1080)
#        self.camera.framerate = 30
#        self.camera.autofocus = False
#        self.camera.awb_mode = 'fluorescent'
#        self.camera.led = False
#        presented = False

    def checkPiIP(self):
        self.ip = netifaces.ifaddresses('eth0')[2][0]['addr']
        print self.ip

    def feed(self):
	   GPIO.output(self.feeder, GPIO.HIGH)       

    def safeQuit(self):
        GPIO.output(self.feeder, True)#changed
        GPIO.cleanup()
        print "GPIOcleanup"
        pygame.quit()
        exit()  


    def mainLoop(self, feedornot):
        while time.time()<self.start:
           #print time.time()-self.start
            pass

        self.startT = time.time()
        fed = False
        while ((time.time() - self.startT) < self.tLength):
            if feedornot == 'yes':
                feed = True
            else:
                feed = False
        self.safeQuit()

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-fd", "--feed", help="feed with this stimulus",action="store_true")
    ap.add_argument("-m:", "--startTime", help="time since epoch that you want to start your trial")
    args = vars(ap.parse_args())
    T = Trial(args["startTime"])
    T.checkPiIP()
    
    if args["feed"]:
        T.mainLoop('yes')
    else:
        T.mainLoop('no')
        
    T.safeQuit()
    print "safequit"
