import Helper
import os
import re

def checkDir():
    curDir = os.getcwd()
    path = "/proc/"
    stringToMatch = "Tgid"
    for pid in range(Helper.getmaxpid()):
        try:
            tempPath = path + str(pid)
            os.chdir(tempPath)
            Tgid = None
            with open('status', 'r') as file:
                for line in file:
                    if stringToMatch in line:
                        Tgid = re.findall(r'\d+', line)[0]
            if (Tgid is not None):
                try:
                    os.chdir(path + Tgid + '/task/' + str(pid))
                except OSError as err:
                    print("Znaleziono Tgid ale w procesie Tgid nie ma takiego pidu {}".format(pid))
            else:
                print("Nie znaleziono Tgid w procesie", pid)
            os.chdir(curDir)
            if Helper.checkps(pid) == False:
                continue
            os.chdir(curDir)
            print("Pid posiada Tgid ale nie znajduje sie w wyniku ps", pid)
        except OSError as err:
            continue
#checkopenDir
#checkreadDir
