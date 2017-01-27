import json
import argparse
import sys
    
if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-p","--pi", help="Name of pi.", required=True)
    ap.add_argument("-cw", "--cwtime",help="Clockwise time (secs).", required=True)
    ap.add_argument("-ccw", "--ccwtime", help="Counter clockwise time (secs)", required=True)

    args = vars(ap.parse_args())

    a_dict = {args["pi"]: {"cwtime": args["cwtime"], "ccwtime": args["ccwtime"]}}
    
    print a_dict
    
    with open('pies.json') as f:
        data = json.load(f)
    
    data.update(a_dict)
    
    with open('pies.json', 'w') as f:
        json.dump(data, f)
    
    sys.exit(0)
