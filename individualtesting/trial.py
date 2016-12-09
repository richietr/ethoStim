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
import sys
from subprocess import call

class Trial:

    def __init__(self, stim,starttime):

        self.stim = stim
        
        self.start = float(starttime)
        self.ip = '127.0.0.1'

        self.feeder = 17 ##
        self.notfeeder = 5 ##



        
    def videoFileName(self, species, tround, sl, sex, fishid, day, session,
                    thatpistimulus, proportion, fedside, correctside):
        self.vidout = ('data/'+str(self.ip)+'/'+(str(species)+'_'+str(tround)
        +'_'+str(sl)+'_'+str(sex) +'_'+str(fishid)+'_'+str(day)+'_'+
        str(session)+'_' +str(self.stim)+'_'+str(thatpistimulus)+'_'+str(proportion)+'_'+str(fedside)+'_'+str(correctside) + '.mkv'))
        print self.vidout
        
        call(["mkdir", "data"])
        call(["mkdir", "data/" + str(self.ip)])
        return self.vidout
    

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

    vidout = T.videoFileName(args["species"], args["round"], args["fishstandardlength"],
                    args["sex"], args["fish"], args["day"], args["session"], args["thatpistimulus"], args["proportion"], args["fedSide"], args["correctside"])  
    
    call(["touch", vidout])
       
    sys.exit(0)
