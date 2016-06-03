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
import datetime
import netifaces

import RPi.GPIO as GPIO
import os.path


#KJW imports
import sys
import select
import os

class Trial:

    def __init__(self, stim,starttime):
        # perhaps replace this with a bash script or RPC that controlls timing
        # of all servers
        #self.now = time.asctime()
        #self.when = when
        #assert self.when - self.now > 0
        #
        pygame.display.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.stimulus = stim
        #
        self.start = float(starttime)
        self.tLength = 30
        self.feedDelay = 10
	#
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

    def whatStimulus(self):
        self.stim, extension = os.path.splitext(self.stimulus)

        if extension == '.png' or extension == '.PNG' or extension == '.jpg' \
        or extension == '.JPG':
        # still image
            try:
                self.image = pygame.image.load('/home/pi/ethoStim/individualtesting/src/'+str(self.stimulus))
            	self.image = pygame.transform.scale(self.image, (640,460))
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
            except IOError:(KeyboardInterrupt           # currently a print should be changed to send a message to
                #the client
                print 'are you sure this file exists? check the src folder \
                ony jpg/JPG, ong/PNG, avi/AVI and mpg/MPG formats'
        '''
    def feed(self):
	GPIO.output(self.feeder, GPIO.HIGH)         
    def notFeed(self):
        GPIO.output(self.notfeeder, GPIO.HIGH)
    def cameraInit(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1280,720)
	self.camera.contrast = 100
        self.camera.brightness = 60
	self.camera.framerate = 25
        self.camera.autofocus = False
	self.camera.exposure_mode = 'auto'
        self.camera.awb_mode = 'off'
	self.camera.awb_gains = (1.8, 1.0)
        self.camera.led = False
        presented = False
	self.camera.rotation = 180
	#self.camera.iso = 800	
        
    def videoFileName(self, species, tround, sl, sex, fishid, day, session,
                    thatpistimulus, proportion, fedside, correctside):
        self.vidout = ('data/'+str(self.ip)+'/'+(str(species)+'_'+str(tround)
        +'_'+str(sl)+'_'+str(sex) +'_'+str(fishid)+'_'+str(day)+'_'+
        str(session)+'_' +str(self.stim)+'_'+str(thatpistimulus)+'_'+str(proportion)+'_'+str(fedside)+'_'+str(correctside)))
        print self.vidout
    
    def startRecording(self):
        self.camera.start_recording(self.vidout+'.mkv', format='h264')
        

    def stopRecording(self):
        self.camera.stop_recording()

    def cameraQuit(self):
        self.camera.close()

    def safeQuit(self):
	GPIO.output(self.feeder, True)#changed
        GPIO.cleanup()
	print "GPIOcleanup"
        pygame.quit()
        exit()

    def mainLoop(self, feedornot):
        ##MATT: set-up feed or not. Dont forget to add it 
        # as a variable in 'mailoop(self, feedornot)'
        if feedornot == 'yes':
            feed = True
        else:
            feed = False


	#delaymet = False
        #presented = False

        while time.time()<self.start:
           #print time.time()-self.start
            pass
        
	self.startT = time.time()
        fed = False
        if args["camera"]:      
            self.startRecording()
        else:
            pass
        while ((time.time() - self.startT) < self.tLength):
           #print (time.time()-self.startT)
	    pygame.display.flip()
	    self.screen.blit(self.image, (40,0))
	    #presented = True
            try:
                
               # if presented == True:
                #    pass
                if (time.time() -self.startT) >  self.feedDelay:
		    #if not fed:
                    #GPIO.setmode(BCM)
		    #GPIO.setmode(GPIO.BCM)
		    #GPIO.setup(17, GPIO.OUT)			
		    #GPIO.output(17, False)
	
                 	#pygame.display.flip()
              	 	#self.screen.blit(self.image, (0,0))
      		 
                 	#presented = True
                    #if fed:
    		        #pass
                    #elif GPIO.event_detected(27):
		        #time.sleep(1.0)
		        #GPIO.output(17,True)
                        #fed = True
			#print "notfed, event detected"
   		    #else:
                      # time.sleep(1.0)
                    ## MATT: turn on either the feeder on the notfeeder here
                    if feed:
                        GPIO.output(self.feeder, False)
                    else:
		        GPIO.output(self.notfeeder, False)  


                       #print time.time()
		  # pass

            except KeyboardInterrupt:
		print'KeyInterrupt'
		self.safeQuit()	
		


if __name__ == '__main__':


    ap = argparse.ArgumentParser()
    ap.add_argument("-f","--fish", help="ID of fish in tank")
    ap.add_argument("-ts", "--thatpistimulus",help="numerosity stimulus being shown on the other raspberry pi in the tank")
    ap.add_argument("-ps", "--pistimulus", help="stimulus being presented with this raspberry pi")
    ap.add_argument("-cs", "--correctside", help="stimulus side on which the correct stimulus is being presented")
    ap.add_argument("-d","--day", help="experiment day, e.g. 1-7")
    ap.add_argument("-s","--session", help="trial session, e.g. 1-4")
    ap.add_argument("-fs","--fedSide", help="side(self.ip feed on/conditioned side")
    ap.add_argument("-x","--sex", help="fish sex")
    ap.add_argument("-p","--proportion", help="ratio that is being presented this trial")
    ap.add_argument("-sp", "--species", help="species name")
    ap.add_argument("-sl","--fishstandardlength", help="standard length of the")
    ap.add_argument("-r","--round", help="training round")
    ap.add_argument("-fd", "--feed", help="feed with this stimulus",action="store_true")
    ap.add_argument("-c", "--camera",help="do you want to record using this pi?",action="store_true")
    ap.add_argument("-m:", "--startTime", help="time since epoch that you want to start your trial")
    args = vars(ap.parse_args())


    T = Trial(args["pistimulus"], args["startTime"])

    
    #T.safeQuit()
    
    T.checkPiIP()
    T.whatStimulus()
    T.videoFileName(args["species"], args["round"], args["fishstandardlength"],
                    args["sex"], args["fish"], args["day"], args["session"], args["thatpistimulus"], args["proportion"], args["fedSide"], args["correctside"])  
    
    #if args["camera"]:
    #T.startRecording()
    #else:
        #pass
    #if args["feed"]:
    if args["camera"]:
        T.cameraInit()

    ## MATT: tell the mainloop yes or no on feeding
    if args["feed"]:
        T.mainLoop('yes')
    else:
        T.mainLoop('no')

    #else:
    #T.mainLoop(False)
    if args["camera"]:
        T.stopRecording()
    else:
        pass  
    
    if args["camera"]:
	T.cameraQuit()

    T.safeQuit() 
    print "safequit"
