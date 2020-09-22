import psutil
import argparse
import json
from datetime import datetime


class jsonFile:

    def __init__(self, state):
        self.state = state

    def add(self):
        with open('json.txt', 'a') as f:
            json.dump(self.state, f, indent=2)


parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Interval between snapshots", type=int, default=30)
parser.add_argument("-t", help="Output file type(json or txt)", default="txt")
args = parser.parse_args()
# ...
if args.t == "json":
    i = 0
    while True:
        currentState = {
            "snapshot": "",
            "date": "",
            "CPU_load(%)": "",
            "disk_usage(%)": "",
            "virtual_memory_usage(%)": ""
        }
        currentState["snapshot"] = str(i + 1)
        currentState["date"] = str(datetime.now())
        currentState["CPU_load(%)"] = str(psutil.cpu_percent(interval=args.i))
        currentState["disk_usage(%)"] = str(psutil.disk_usage('/').percent)
        currentState["virtual_memory_usage(%)"] = str(psutil.virtual_memory().percent)
        # with open('json.txt', 'a') as f:
        # 	json.dump(currentState, f, indent = 2)
        jsF = jsonFile(currentState)
        jsF.add()
        i += 1
elif args.t == "txt" or args.t == "":
    i = 0
    while True:
        cpuLoad = str(psutil.cpu_percent(interval=args.i))
        memUsage = str(psutil.disk_usage('/').percent)
        virtualMemUsage = str(psutil.virtual_memory().percent)
        # print("SNAPSHOT%d" % (i+1), datetime.now(), cpuLoad, memUsage, virtualMemUsage, sep=" : ")
        txt = open("txt.txt", "a")
        txt.write("SNAPSHOT%d : %s : %s pct : %s pct : %s pct\n"
                  % (i + 1, datetime.now(), cpuLoad, memUsage, virtualMemUsage))
        i += 1
else:
    print("Incorrect file type!\nTry 'txt' or 'json'...")
