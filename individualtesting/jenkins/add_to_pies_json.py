import json
import argparse
import sys
    
if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-p","--pi", help="Name of pi.", required=True)
    ap.add_argument("-cw", "--cwtime",help="Clockwise time (secs).", required=True)
    ap.add_argument("-ccw", "--ccwtime", help="Counter clockwise time (secs)", required=True)

    args = vars(ap.parse_args())

    pi = args["pi"]
    a_dict = {pi: {"cwtime": args["cwtime"], "ccwtime": args["ccwtime"]}}
    
    #print a_dict
    
    with open('pies.json') as f:
        data = json.load(f)
    
    if pi in data:
        print 'ERROR> ' + pi + ' is already in pies.json!'
        print 'Remove pi before adding!'
        sys.exit(1)
        
    data.update(a_dict)
    
    with open('pies.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))
    
    print 'SUCCESS> ' + pi + ' was added to pies.json'
    
    sys.exit(0)
