import re
import os
import subprocess
import signal
import datetime

def tail():
    out, err = subprocess.Popen(['tail','-n','10','/var/log/kern.log'], stdout=subprocess.PIPE).communicate()
    out = out.splitlines()
    currentDT = datetime.datetime.now()
    print (str(currentDT.strftime("%b %d %H:%M:%S")))
    #currentDT = currentDT - datetime.timedelta(minutes=1)
    matchTag = currentDT.strftime("%b %d %H:%M:%S")
    for line in out:
        if re.search(r'\b{}\b'.format(matchTag), line.decode("utf-8")):
            print(line.decode("utf-8"))

def KernelModule():

    if os.geteuid() == 0:
        subprocess.call(['insmod','Main.ko'], stdout=subprocess.PIPE)
        linesCount = 4
        tail()
        if os.geteuid() == 0:
            subprocess.call(['rmmod','Main.ko'], stdout=subprocess.PIPE)
    else:
        print("Brak Uprawnien administratora")
