import json
import argparse
import sys
    
if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-f","--fish", help="Name of fish.", required=True)

    args = vars(ap.parse_args())

    fish = args["fish"]
    
    with open('fish.json') as f:
        data = json.load(f)
    
    if fish not in data:
        print 'ERROR> ' + fish + ' is not in fish.json'
        sys.exit(1)
        
    data.pop(fish, None)
    
    with open('fish.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))
    
    print 'SUCCESS> ' + fish + ' was removed from fish.json'
    sys.exit(0)