import os
import sys
import subprocess
import Core.Helper as Helper

def BruteForcePidsByFork():
    print("Sprawdzenie wyniku programu ps poprzez tworzenie nowych procesow")
    listpid = list();
    maxpid = Helper.getmaxpid()

    for kern in range (0,301):
        listpid.append(0)

    for proc in range (301,maxpid):
        listpid.append(proc)

    for x in range(301,maxpid):
        try:
            pid = os.fork()
            if(pid == 0):
                os._exit(0)
            listpid[pid] = 0
            os.waitpid(pid,0)
        except:
            continue

    for p in range(0,maxpid):
        if (listpid[p] is not 0):
            if Helper.checkps(listpid[p]):
                print("Ukryty process o identyfikatorze {}".format(p))
#thread
