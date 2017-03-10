import json
import csv
import argparse

if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-i","--csvfile", help="Input csv file.", required=True)
    ap.add_argument("-o", "--jsonfile",help="Output json file.", required=True)
    args = vars(ap.parse_args())
    
    jsonfile = args['jsonfile']
    csvfile = args['csvfile']
        
    # open csv file for reading
    thiscsv = open(csvfile, "rb")
    reader = csv.reader(thiscsv)
    
    # remove the header line
    newlist = []
    reader.next()
    for r in reader:
        newlist.append(r)
    
    # sort by trial number
    sortedlist = sorted(newlist, key=lambda row: int(row[0]), reverse=False)
    
    # loop through list, create dict format, and append to json dict
    jsonData = {}
    for i in sortedlist:
        trialnumber = i[0]
        day = i[1]
        time = i[2]
        thatpistimulus = i[3]
        pistimulus = i[4]
        correctside = i[5]
        session = i[6]
        feedside = i[7]
        proportion = i[8]
        feed = i[9]
        camera = i[10]
        a_dict = {int(trialnumber): {"day": day, "time": time, "thatpistimulus": thatpistimulus, "pistimulus": pistimulus,
                                "correctside": correctside, "session": session, "feedside": feedside, 
                                "proportion": proportion, "feed": feed, "camera": camera}}
        jsonData.update(a_dict)
    
    # write to json file
    with open(jsonfile, 'w') as f:
        json.dump(jsonData, f, sort_keys=True, indent=4, separators=(',', ': '))
    
    # close csv file
    thiscsv.close()