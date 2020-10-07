import os


listpid = list();

f = open("/proc/sys/kernel/pid_max")
maxpid = f.read()
for x in range(int(10)):
    try:
        pid = os.fork()
        if(pid == 0):
            os._exit(0)
        listpid.append(pid)
        os.waitpid(pid,0)
    except:
        pass
for p in set(listpid):
    print(p)
