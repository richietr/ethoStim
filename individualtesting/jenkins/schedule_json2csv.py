import json
import csv
import argparse

if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-i","--jsonfile", help="Input json file.", required=True)
    ap.add_argument("-o", "--csvfile",help="Output csv file.", required=True)
    args = vars(ap.parse_args())
    
    jsonfile = args['jsonfile']
    csvfile = args['csvfile']
    
    # open and load json file
    with open(jsonfile) as f:
        data = json.load(f)
    
    # open csv file for writing
    thiscsv = open(csvfile, "wb")
    
    # create the writer
    writer = csv.writer(thiscsv)
    
    # loop through all trials and write values
    for trialnum in data:
        writer.writerow((trialnum, data[trialnum]['day'], data[trialnum]['time'], data[trialnum]['thatpistimulus'], \
                         data[trialnum]['pistimulus'], data[trialnum]['correctside'], data[trialnum]['session'], \
                         data[trialnum]['feedside'], data[trialnum]['proportion'], data[trialnum]['feed'], \
                         data[trialnum]['camera']))
    
    # close csv file
    thiscsv.close()
    
    # re-open csv file for reading
    thiscsv = open(csvfile, "rb")
    reader = csv.reader(thiscsv)
    
    # sort by trial number
    sortedlist = sorted(reader, key=lambda row: int(row[0]), reverse=False)
    
    # close csv file
    thiscsv.close()
    
    # re-open csv file for writing sorted list
    thiscsv = open(csvfile, "wb")
    writer = csv.writer(thiscsv)
    
    # add the header
    writer.writerow(('trial','day','time','thatpistimulus','pistimulus','correctside',\
                     'session','feedside','proportion','feed','camera'))
    writer.writerows(sortedlist)
    
    # close csv file
    thiscsv.close()
    
    print 'Success!'