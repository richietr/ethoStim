import json
import argparse
import sys
import os

if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-n1", "--node1", help="Node 1 that will be clean", required=True)
    ap.add_argument("-n2", "--node2", help="Node 2 that will be clean", required=True)
    ap.add_argument("-n3", "--node3", help="Node 3 that will be clean", required=True)
    ap.add_argument("-n4", "--node4", help="Node 4 that will be clean", required=True)
    ap.add_argument("-n5", "--node5", help="Node 5 that will be clean", required=True)
    ap.add_argument("-n6", "--node6", help="Node 6 that will be clean", required=True)
    ap.add_argument("-n7", "--node6", help="Node 7 that will be clean", required=True)
    ap.add_argument("-n8", "--node6", help="Node 8 that will be clean", required=True)
    ap.add_argument("-n9", "--node6", help="Node 9 that will be clean", required=True)
    ap.add_argument("-n10", "--node6", help="Node 10 that will be clean", required=True)
    ap.add_argument("-n11", "--node6", help="Node 11 that will be clean", required=True)
    ap.add_argument("-n12", "--node6", help="Node 12 that will be clean", required=True)

    args = vars(ap.parse_args())

    a_dict = {"node1": args["node1"], "node2": args["node2"], "node3": args["node3"], "node4": args["node4"], "node5": args["node5"], "node6": args["node6"], "node7": args["node7"], "node8": args["node8"], "node9": args["node9"], "node10": args["node10"], "node11": args["node11"], "node12": args["node12"]}

    #print a_dict

    os.remove('trashcan.json')

    with open('trashcan.json', 'w') as f:
        json.dump(a_dict, f, sort_keys=True, indent=4, separators=(',', ': '))

    sys.exit(0)
