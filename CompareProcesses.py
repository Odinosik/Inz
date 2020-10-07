import subprocess
import os
import signal


def CompareProcPs():
    print("Porownanie zawartosci katalogu /proc z wynikiem programu ps")

    out, err = subprocess.Popen(['ps', '-A', '-o', 'pid'], stdout=subprocess.PIPE).communicate()
    out = out.splitlines()
    list = []
    for a in out:
        list.append(a.strip())
    path = "/proc"
    list.pop();
    list.remove(list[0])

    list_proc = []

    files = os.listdir(path)
    for pid in list:
        if pid.decode("utf-8") not in files:
            print(str(pid))
            list_proc.append(str(pid))
            print("PID numer nie znajduje sie w /proc")
    if not list_proc:
        print("Nie znaleziono ukrytych procesow")
    else:
        print("Ukryte procesy pod pidem:")
        for hideProc in list_proc:
            print(str(hideProc.decode("utf-8")))


#os.kill(os.getpid(), signal.SIGKILL)
#WyLISTOWANIE PIDOW PROCESSOW PRZEZ PS
