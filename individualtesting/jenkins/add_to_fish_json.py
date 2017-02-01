import json
import argparse
import sys
    
if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-f","--fish", help="Name of fish.", required=True)
    ap.add_argument("-sp", "--species",help="Species of fish.", required=True)
    ap.add_argument("-s", "--sex", help="Sex of fish", required=True)
    ap.add_argument("-sl", "--fishstandardlength", help="Standard length of fish", required=True)
    ap.add_argument("-n","--node", help="Node without camera", required=True)
    ap.add_argument("-c","--camnode", help="Node with camera", required=True)

    args = vars(ap.parse_args())

    fish = args["fish"]
    
    a_dict = {fish: {"species": args["species"], "sex": args["sex"], "fishstandardlength": args["fishstandardlength"], "node": args["node"], "cam_node": args["camnode"]}}
    
    #print a_dict
    
    with open('fish.json') as f:
        data = json.load(f)
    
    if fish in data:
        print 'ERROR> ' + fish + ' is already in fish.json!'
        print 'Remove fish before adding!'
        sys.exit(1)
        
    data.update(a_dict)
    
    with open('fish.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))
    
    print 'SUCCESS> ' + fish + ' was added to fish.json'
    
    sys.exit(0)