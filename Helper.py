import subprocess
import os

def checkthread(pid):
    command = "ps -eLf | awk \'{ print $4 }\'"
    out, err = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()
    out = out.splitlines()
    list = []
    for a in out:
        list.append(a.strip().decode("utf-8"))
    if (str(pid) not in list):
        return True
    else:
        return False

def checkps(pid):
    command = "ps -eLf | awk \'{ print $2 }\'"
    out, err = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()
    out = out.splitlines()
    list = []
    for a in out:
        list.append(a.strip().decode("utf-8"))
    if (str(pid) not in list):
        return checkthread(pid)
    else:
        return False


def getmaxpid():
    f = open("/proc/sys/kernel/pid_max")
    maxpid = f.read()
    return int(maxpid) - 1

def checkPermission():
    if os.geteuid() == 0:
        return True
    else:
        return False
