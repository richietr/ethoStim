import json
import os
import sys
import types
import datetime
from itertools import groupby

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
    def isFishInFishJson(self, fish):
        if fish in self.fish_dict:
            print self.me + ': ' + fish + ' is valid (in fish.json)'
            return True
        print self.me + ': ERROR> ' + fish + ' is NOT valid (NOT in fish.json'
        return False
    
    @staticmethod
    def runIsFishValidTest(self):
        print '\n', '*' * 50
        print '*' * 14, ' Fish Validity Test ', '*' * 14
        print '*' * 50 
        results = []
        fish_list = []
        # Check if mapping is in top.json
        if 'mapping' in self.top_dict:
            # Check if all fish in mapping are in fish.json
            tmp_dict = self.top_dict['mapping']
            for sch in self.schedules:
                if sch in tmp_dict:
                    results.append(self.isFishInFishJson(self, tmp_dict[sch]))
                    fish_list.append(tmp_dict[sch])
                else:
                    print self.me + ': Error> Schedule ' + sch + ' is not in mapping, issue with top.json'
                    print self.me + ': Exiting...'
                    sys.exit(1)                     
        else:
            print self.me + ': Error> Mapping is not in top_dict, issue with top.json'
            print self.me + ': Exiting...'
            sys.exit(1) 
        
        # Check if any fish are assigned to more than 1 schedule
        tmp = [len(list(group)) for key, group in groupby(fish_list)]
        if (all(i == 1 for i in tmp)):
            print self.me + ': All fish are assigned to only 1 schedule'
            results.append(True)
        else:
            print self.me + ': ERROR> One or more fish are assigned to multiple schedules'
            results.append(False)
        
        if False in results:
            print '\nFish Validity Test Result: FAIL'           
            print '*' * 50        
            return False
        print '\nFish Validity Test Result: PASS'         
        print '*' * 50
        return True
    
    @staticmethod
    def runIsDateValidTest(self):
        DAYS_LIMIT = 30
        print '\n', '*' * 50
        print '*' * 14, ' Date Validity Test ', '*' * 14
        print '*' * 50 
        results = []
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Check if start date is in top.json
        if 'startDate' in self.top_dict:
            # Get today's date
            now = datetime.datetime.now()
            now_month = now.month
            now_day = now.day        
            print self.me + ': Current date/time is ' + str(now)
            start_date = self.top_dict['startDate'].split('/')
            start_month = int(start_date[0])
            start_day = int(start_date[1])
            # Check if start month is this month or next
            if now_month is not 12:
                print self.me + ': Is start month either this month or next? ' + str((start_month == now_month or start_month == now_month + 1))
                results.append(start_month == now_month or start_month == now_month + 1)
            else:
                print self.me + ': Is start month either this month or next? ' + str((start_month == 12 or start_month == 1))
                results.append(start_month == 12 or start_month == 1)
            # Check if within 30 days
            now_days = now_day
            for i in range(1,now_month):
                now_days = now_days + days_in_month[i-1]
            start_days = start_day
            for i in range(1,start_month):
                start_days = start_days + days_in_month[i-1]
            total_days = 0
            for i in range(1,13):
                total_days = total_days + days_in_month[i-1]
            result = False
            if now_days < total_days-30:
                result = (now_days < start_days and start_days < now_days + DAYS_LIMIT)
            else:
                if(start_month == 12 and now_month == 12):
                    result = True
                else:
                    days_left = total_days - now_days
                    if days_left + start_days < DAYS_LIMIT:
                        result = True
            print self.me + ': Is start date within next 30 days? ' + str(result)
            results.append(result)                            
        else:
            print self.me + ': Error> Start date is not in top_dict, issue with top.json'
            print self.me + ': Exiting...'
            sys.exit(1) 
        
        if False in results:
            print '\nDate Validity Test Result: FAIL'           
            print '*' * 50        
            return False
        print '\nDate Validity Test Result: PASS'         
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
        
        # Test decode and launch
        for test in self.test_list:
            if test is 'fish_is_valid':
                results.append(self.runIsFishValidTest(self))
            elif test is 'date_is_valid':
                results.append(self.runIsDateValidTest(self))
        
        # Determine overall result
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
        print '*' * 50, '\n' 
        sys.exit(1)
    
    print('Passed Validation!')
    print("Exiting with Error Code 0")
    print '*' * 50, '\n' 
    sys.exit(0)