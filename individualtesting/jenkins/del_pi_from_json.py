import json
import argparse
import sys
    
if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-p","--pi", help="Name of Pi.", required=True)

    args = vars(ap.parse_args())

    pi = args["pi"]
    
    with open('pies.json') as f:
        data = json.load(f)
    
    if pi not in data:
        print 'ERROR> ' + pi + ' is not in pies.json'
        sys.exit(1)
        
    data.pop(pi, None)
    
    with open('pies.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))
    
    print 'SUCCESS> ' + pi + ' was removed from pies.json'
    sys.exit(0)