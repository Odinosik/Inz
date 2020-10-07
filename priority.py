import subprocess
import os
import Helper

def priority():
    print("Sprawdzenie wszystkich pidow z wykorzystaniem getpriority()")
    maxpid = Helper.getmaxpid()
    for pid in range(maxpid):
        try:
            ret = os.getpriority(os.PRIO_PROCESS,pid)
            if(Helper.checkps(pid)):
                ret2 = os.getpriority(os.PRIO_PROCESS,pid)
                print("Process o identyfikatorze {} nie zawiera sie w wyniku programu ps".format(pid))
        except OSError as err:
            continue

def gegid():
    print("Sprawdzenie wszystkich pidow z wykorzystaniem getpgid()")
    maxpid = Helper.getmaxpid()
    for pid in range(maxpid):
        try:
            ret = os.getpgid(pid)
            if(Helper.checkps(pid)):
                ret2 = os.getpgid(pid)
                print("Process o identyfikatorze {} nie zawiera sie w wyniku programu ps".format(pid))
        except OSError as err:
            continue

def getsid():
    print("Sprawdzenie wszystkich pidow z wykorzystaniem getsid()")
    maxpid = Helper.getmaxpid()
    for pid in range(maxpid):
        try:
            ret = os.getsid(pid)
            if(Helper.checkps(pid)):
                ret2 = os.getsid(pid)
                print("Process o identyfikatorze {} nie zawiera sie w wyniku programu ps".format(pid))
        except OSError as err:
            continue

def sched_getaffinity():
    print("Sprawdzenie wszystkich pidow z wykorzystaniem sched_getparam()")
    maxpid = Helper.getmaxpid()
    for pid in range(maxpid):
        try:
            ret = os.sched_getparam(pid)
            if(Helper.checkps(pid)):
                ret2 = os.sched_getparam(pid)
                print("Process o identyfikatorze {} nie zawiera sie w wyniku programu ps".format(pid))
        except OSError as err:
            continue

def sched_getaffinity():
    print("Sprawdzenie wszystkich pidow z wykorzystaniem sched_getparam()")
    maxpid = Helper.getmaxpid()
    for pid in range(maxpid):
        try:
            ret = os.checksched_rr_get_interval(pid)
            if(Helper.checkps(pid)):
                ret2 = os.sched_rr_get_interval(pid)
                print("Process o identyfikatorze {} nie zawiera sie w wyniku programu ps".format(pid))
        except OSError as err:
            continue

def checkkill():
    print("Sprawdzenie wszystkich pidow z wykorzystaniem sched_getparam()")
    maxpid = Helper.getmaxpid()
    for pid in range(maxpid):
        try:
            ret = os.kill(pid,0)
            if(Helper.checkps(pid)):
                ret2 = os.kill(pid)
                print("Process o identyfikatorze {} nie zawiera sie w wyniku programu ps".format(pid))
        except OSError as err:
            continue
def CheckAll():
    print("Sprawdzenie wszystkich pidow z wykorzystaniem sched_getparam()")
    maxpid = Helper.getmaxpid()
    for pid in range(maxpid):
        check = 0
        try:
            kill = os.kill(pid,0)
            check += 1
            interval = os.sched_rr_get_interval(pid)
            check += 1
            param = os.sched_getparam(pid)
            check += 1
            priority = os.getpriority(os.PRIO_PROCESS,pid)
            check += 1
            sid = os.getsid(pid)
            check += 1
            kill2 = os.kill(pid,0)
            if (Helper.checkps(pid)):
                print("Ukryty process o identyfikatorze {}".format(pid))
        except OSError as err:
            if (check is not 0):
                print("Ukryty process o identyfikatorze {}".format(pid), check)
            continue
