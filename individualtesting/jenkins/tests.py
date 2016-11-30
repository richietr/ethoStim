import json
import os
import sys
import types

def parseTopJSON():
    with open(os.path.join('top.json'), 'r') as jsonFile:
        jsonString = jsonFile.read()
        paramsDict = json.loads(jsonString)
        for k,v in paramsDict.iteritems():
            if type(v) == types.UnicodeType:    
                path_elems = v.split('\\')
                newPath = os.path.join(*path_elems)
                paramsDict[k] = newPath
    top_dict = paramsDict
    
    # check error conditions           
    if top_dict is None:
        print 'Tests: Error> Top dictionary is None, problem parsing top.json'
        print 'Tests: Exiting...'
        sys.exit(1)
    
    return top_dict
                  
def parseFishJSON():
    with open(os.path.join('fish.json'), 'r') as jsonFile:
        jsonString = jsonFile.read()
        paramsDict = json.loads(jsonString)
        for k,v in paramsDict.iteritems():
            if type(v) == types.UnicodeType:    
                path_elems = v.split('\\')
                newPath = os.path.join(*path_elems)
                paramsDict[k] = newPath
    fish_dict = paramsDict
    
    # check error conditions           
    if fish_dict is None:
        print 'Tests: Error> Fish dictionary is None, problem parsing fish.json'
        print 'Tests: Exiting...'
        sys.exit(1) 
    
    return fish_dict       
                        
def parseTestsJSON():        
    with open(os.path.join('tests.json'), 'r') as jsonFile:
        jsonString = jsonFile.read()
        paramsDict = json.loads(jsonString)
        for k,v in paramsDict.iteritems():
            if type(v) == types.UnicodeType:    
                path_elems = v.split('\\')
                newPath = os.path.join(*path_elems)
                paramsDict[k] = newPath
                
#         key = 'TempStepSize'    
#         if key in paramsDict:
#             if Tests.checkIfNumber(paramsDict[key]):
#                 self.tempStepSize = int(paramsDict[key])
#             else:
#                 print self.me + ': Error> ' + key + ' is not numeric, will use default'
#         else:
#             print self.me + ': Error> ' + key + ' is not in parameters.json, will use default'
                 
    key = 'test_list'  
    test_list = []
    if key in paramsDict:
        tmp_list = eval(paramsDict[key])
        for k in tmp_list:
            if tmp_list[k] is "True":
                test_list.append(k)
    else:
        print 'Tests: Info> ' + key + ' is not in tests.json, NO TESTS WILL BE RUN!'
        print 'Tests: Exiting...'
        sys.exit(0)

    # Check error conditions           
    if not test_list:
        print 'Tests: Info> Test list is empty, NO TESTS WILL BE RUN!'
        print 'Tests: Exiting...'
        sys.exit(0) 
        
    return test_list

class Tests(object):
    
    #DEFAULT_MIN_TEMP = -10

    def __init__(self):
        self.me = 'Tests'
        #self.startTemp = Tests.DEFAULT_MIN_TEMP        
        self.top_dict = parseTopJSON()
        self.fish_dict = parseFishJSON()
        self.test_list = parseTestsJSON()     
        self.schedules = ["H1", "H2", "H3", "L1", "L2", "L3"]
    
    @staticmethod
    def checkIfNumber(s):
        if s[0] in ('-','+'):
            return s[1:].isdigit()
        return s.isdigit()  
    
    @staticmethod
    def isFishValid(self, fish):
        if fish in self.fish_dict:
            print self.me + ': ' + fish + ' is valid'
            return True
        print self.me + ': ' + fish + ' is NOT valid'
        return False
    
    @staticmethod
    def runIsFishValidTest(self):
        print '\n', '*' * 50
        print '*' * 14, ' Fish Validity Test ', '*' * 14
        print '*' * 50 
        results = []
        if 'mapping' in self.top_dict:
            tmp_dict = self.top_dict['mapping']
            for sch in self.schedules:
                if sch in tmp_dict:
                    results.append(self.isFishValid(self, tmp_dict[sch]))
                else:
                    print self.me + ': Error> Schedule ' + sch + ' is not in mapping, issue with top.json'
                    print self.me + ': Exiting...'
                    sys.exit(1)                     
        else:
            print self.me + ': Error> Mapping is not in top_dict, issue with top.json'
            print self.me + ': Exiting...'
            sys.exit(1) 
            
        if False in results:
            print '\nFish Validity Test Result: FAIL'           
            print '*' * 50        
            return False
        print '\nFish Validity Test Result: PASS'         
        print '*' * 50
        return True
    
    def runTests(self):                
        # Print out tests to run
        print '\n', '*' * 50
        print('Tests to run:')
        for test in self.test_list:
            print test
        print '*' * 50, '\n' 
        
        results = []
        
        for test in self.test_list:
            if test is 'fish_is_valid':
                results.append(self.runIsFishValidTest(self))
            
        if False in results:
            print '\nOverall Test Result: FAIL\n'          
            return False
        print '\nOverall Test Result: PASS\n' 
        return True
                
                    
if __name__ == '__main__':
    
    test = Tests()
    result = test.runTests()
    if result is False:
        print('Failed Validation!')
        print("Exiting with Error Code 1")
        sys.exit(1)
    
    print('Passed Validation!')
    print("Exiting with Error Code 0")
    sys.exit(0)