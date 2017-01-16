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
import sys
import os

def getIpAddr():
   ip = netifaces.ifaddresses('eth0')[2][0]['addr']
   print ip
   return ip

class Trial:

    def __init__(self, stim, starttime):
        
        pygame.display.init()
        pygame.mouse.set_visible(False)
        
        self.vidout = None
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.stimulus = stim
        self.start = float(starttime)
        self.tLength = 3
        self.feedDelay = 10
        self.notch = 0.47
        self.feeder = 17
        self.notfeeder = 27
        self.ip = None
        
        # Configure RPi GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.feeder, GPIO.OUT)
        GPIO.setup(self.notfeeder, GPIO.OUT)
        print "GPIOinit"

    def whatStimulus(self):
        self.stim, extension = os.path.splitext(self.stimulus)
        if extension == '.png' or extension == '.PNG' or extension == '.jpg' or extension == '.JPG':
        # still image
            try:
                self.image = pygame.image.load('src/' + str(self.stimulus))
                self.image = pygame.transform.scale(self.image, (640, 460))
            except IOError:
                print 'Are you sure this file exists? check the src folder \
                ony jpg/JPG, png/PNG formats'
    
    @staticmethod            
    def turnOnFeeders(self):
        GPIO.output(self.notfeeder, 1)
        GPIO.output(self.feeder, 1)
        print 'turnOnFeeders'
        
    @staticmethod
    def turnOffFeeders(self):
        GPIO.output(self.feeder, 0)         
        GPIO.output(self.notfeeder, 0) 
        print 'turnOffFeeders'
    
    @staticmethod   
    def cameraInit(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1280, 720)
        self.camera.contrast = 100
        self.camera.brightness = 75
        self.camera.framerate = 25
        # self.camera.autofocus = False
        self.camera.exposure_mode = 'auto'
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = (1.8, 1.0)
        self.camera.led = False
        presented = False
        self.camera.rotation = 180
        # self.camera.iso = 800    
        
    def videoFileName(self, species, tround, sl, sex, fishid, day, session,
                    thatpistimulus, proportion, fedside, correctside):
        # TODO: Remove data/<ip> whenever switch to jenkins occurs
        #self.vidout = ('data/' + str(self.ip) + '/' + (str(species) + '_' + str(tround)
        #               + '_' + str(sl) + '_' + str(sex) + '_' + str(fishid) + '_' + str(day) + '_' + 
        #               str(session) + '_' + str(self.stim) + '_' + str(thatpistimulus) + '_' + 
        #               str(proportion) + '_' + str(fedside) + '_' + str(correctside) + '.mkv'))
        self.vidout = ((str(species) + '_' + str(tround)
                       + '_' + str(sl) + '_' + str(sex) + '_' + str(fishid) + '_' + str(day) + '_' + 
                       str(session) + '_' + str(self.stim) + '_' + str(thatpistimulus) + '_' + 
                       str(proportion) + '_' + str(fedside) + '_' + str(correctside) + '.mkv'))
        print self.vidout
        return self.vidout
    
    @staticmethod
    def startRecording(self):
        self.camera.start_recording(self.vidout, format='h264')
    
    @staticmethod    
    def stopRecording(self):
        self.camera.stop_recording()
    
    @staticmethod
    def cameraQuit(self):
        self.camera.close()

    def safeQuit(self):
        # Ensure feeders are OFF
        self.turnOffFeeders(self)
        GPIO.cleanup()
        print "GPIOcleanup"
        pygame.quit()
        sys.exit()

    def runSingleTrial(self, feed, use_camera):
        
        fed = False
        
        # Initialize camera
        if use_camera:
            self.cameraInit(self)
        
        # Wait for start time
        while time.time() < self.start:
           # print time.time()-self.start
            pass
        
        # Note time that trial really starts
        self.startT = time.time()
        
        # Turn on screen and wait 2 secs
        pygame.display.flip()
        self.screen.blit(self.image, (40, 0))
        time.sleep(2)   
           
        # Start recording
        if use_camera:      
            self.startRecording(self)
        
        # Wait until record length is reached    
        while ((time.time() - self.startT) < self.tLength):
           # print (time.time()-self.startT)
        
           # Wait and feed (if applicable)
           try:
               if (time.time() - self.startT) > self.feedDelay:
                   if feed:
                       # Turn feeders on
                       self.turnOnFeeders(self)
                       # Wait for notch time
                       print 'Sleep ' + str(self.notch) + ' secs'
                       time.sleep(self.notch)
                       # Turn feeders off
                       self.turnOffFeeders(self)
		       print 'Sleep ' + str(3) + ' secs'
                       time.sleep(3)
		       self.turnOnFeeders(self)
		       print 'Sleep ' + str(self.notch) + ' secs'
                       time.sleep(self.notch)
		       self.turnOffFeeders(self)
		       feed = False
           except KeyboardInterrupt:
               print'KeyInterrupt'
               safeQuit()           
    
        # Stop recording and close camera
        if use_camera:
            self.stopRecording(self)
            self.cameraQuit(self)        


if __name__ == '__main__':

    use_camera = False
    feed = False
    video_file = 'N/A'

    os.environ["DISPLAY"] = ":0.0" 

    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--fish", help="ID of fish in tank")
    ap.add_argument("-ts", "--thatpistimulus", help="numerosity stimulus being shown on the other raspberry pi in the tank")
    ap.add_argument("-ps", "--pistimulus", help="stimulus being presented with this raspberry pi")
    ap.add_argument("-cs", "--correctside", help="stimulus side on which the correct stimulus is being presented")
    ap.add_argument("-d", "--day", help="experiment day, e.g. 1-7")
    ap.add_argument("-s", "--session", help="trial session, e.g. 1-4")
    ap.add_argument("-fs", "--fedSide", help="side feed on/conditioned side")
    ap.add_argument("-x", "--sex", help="fish sex")
    ap.add_argument("-p", "--proportion", help="ratio that is being presented this trial")
    ap.add_argument("-sp", "--species", help="species name")
    ap.add_argument("-sl", "--fishstandardlength", help="standard length of the")
    ap.add_argument("-r", "--round", help="training round")
    ap.add_argument("-fd", "--feed", help="feed with this stimulus", action="store_true")
    ap.add_argument("-c", "--camera", help="do you want to record using this pi?", action="store_true")
    ap.add_argument("-m:", "--startTime", help="time since epoch that you want to start your trial")
    args = vars(ap.parse_args())


    T = Trial(args["pistimulus"], args["startTime"])
    
    T.ip = getIpAddr()
    T.whatStimulus()
    
    # Set video filename
    video_file = T.videoFileName(args["species"], args["round"], args["fishstandardlength"],
                    args["sex"], args["fish"], args["day"], args["session"], args["thatpistimulus"], args["proportion"], args["fedSide"], args["correctside"])  
        
    # Write video file name out to temp.txt, needed by Jenkins
    f = open("temp.txt", "w")
    f.write(video_file)
    f.close()
        
    # Determine if camera will be used
    if args["camera"]:
        use_camera = True
    
    # Determine if feeding is needed
    if args["feed"]:
        feed = True
    
    # Record video and feed
    T.runSingleTrial(feed, use_camera)

    # Cleanup and Exit
    T.safeQuit() 
    print "safequit"
