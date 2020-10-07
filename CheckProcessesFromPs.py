import subprocess
import os

def checkStatusDirectory(process):
    stat = os.stat('/proc/' + str(process))

def killzero(process):
    os.kill(process,0)

def CheckProcessesFromPs():
        print("Porownanie informacji zebranych z programu ps z informacjami z procfs")
        out, err = subprocess.Popen(['ps', '-A', '-o', 'pid'], stdout=subprocess.PIPE).communicate()
        out = out.splitlines()
        list = []
        for a in out:
            list.append(a.strip())

        path = "/proc"
        list.pop();
        list.remove(list[0])
        list_find_proc = []
        for process in list:
            try:
                pgid = os.getpgid(int(process))
                sid = os.getsid(int(process))
                schedular = os.sched_getscheduler(int(process))
                param = os.sched_getparam(int(process))
                checkStatusDirectory(int(process))
                killzero(int(process))
            except OSError as err:
                list_find_proc.append(process)
                continue

        if not list_find_proc:
            print("Nie znaleziono ukrytych processow")
        else:
            print("Ukryte procesy pod pidem:")
            for hideProc in list_find_proc:
                print(str(hideProc.decode("utf-8")))



    #os.kill(os.getpid(), signal.SIGKILL)
