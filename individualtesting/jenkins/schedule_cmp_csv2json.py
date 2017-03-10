import json
import csv
import argparse
import sys

if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-j","--jsonfile", help="Input json file.", required=True)
    ap.add_argument("-c", "--csvfile",help="Input csv file.", required=True)
    args = vars(ap.parse_args())
    
    jsonfile = args['jsonfile']
    csvfile = args['csvfile']
    
    # open and load json file
    with open(jsonfile) as f:
        data = json.load(f)
        
    # open csv file for reading
    thiscsv = open(csvfile, "rb")
    reader = csv.reader(thiscsv)
    
    # remove the header line from csv
    newlist = []
    reader.next()
    for r in reader:
        newlist.append(r)
    
    # sort by trial number
    sortedlist = sorted(newlist, key=lambda row: int(row[0]), reverse=False)
    
    # column numbers in csv
    trialnum_col = 0
    day_col = 1
    time_col = 2
    thatpistimulus_col = 3
    pistimulus_col = 4
    correctside_col = 5
    session_col = 6
    feedside_col = 7
    proportion_col = 8
    feed_col = 9
    camera_col = 10
    
    error = False
    
    # Check if json and csv match
    for i in sortedlist:
        # First check if trial number from csv is in json
        if not data.has_key(i[trialnum_col]):
            print 'ERROR> json file is missing trial number ' + i[trialnum_col]
            error = True
        else:
            trialnum = i[trialnum_col]
            if i[day_col] != data[trialnum]['day']:
                print 'ERROR> Trial #' + i[trialnum_col] + ' day mismatch!'
                error = True
            if i[time_col] != data[trialnum]['time']:
                print 'ERROR> Trial #' + i[trialnum_col] + ' time mismatch!'
                error = True
            if i[thatpistimulus_col] != data[trialnum]['thatpistimulus']:
                print 'ERROR> Trial #' + i[trialnum_col] + ' thatpistimulus mismatch!'
                error = True
            if i[pistimulus_col] != data[trialnum]['pistimulus']:
                print 'ERROR> Trial #' + i[trialnum_col] + ' pistimulus mismatch!'
                error = True
            if i[correctside_col] != data[trialnum]['correctside']:
                print 'ERROR> Trial #' + i[trialnum_col] + ' correctside mismatch!'
                error = True
            if i[session_col] != data[trialnum]['session']:
                print 'ERROR> Trial #' + i[trialnum_col] + ' session mismatch!'
                error = True
            if i[feedside_col] != data[trialnum]['feedside']:
                print 'ERROR> Trial #' + i[trialnum_col] + ' feedside mismatch!'
                error = True
            if i[proportion_col] != data[trialnum]['proportion']:
                print 'ERROR> Trial #' + i[trialnum_col] + ' proportion mismatch!'
                error = True
            if i[feed_col] != data[trialnum]['feed']:
                print 'ERROR> Trial #' + i[trialnum_col] + ' feed mismatch!'
                error = True
            if i[camera_col] != data[trialnum]['camera']:
                print 'ERROR> Trial #' + i[trialnum_col] + ' camera mismatch!'
                error = True
    
    if len(sortedlist) != len(data):
        print 'ERROR> csv file and json file have different number of trials!'
        error = True
    
    if not error:
        print 'SUCCESS> CSV and JSON have matching data!'
        sys.exit(0)
    else:
        print 'ERROR> CSV and JSON do NOT have matching data!'
        sys.exit(1)