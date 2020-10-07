import CompareProcesses
import CheckProcessesFromPs
import kernel_module
import os
import BruteForcePids
import priority
import sys
import Helper
import CheckProcfs
import argparse

def one():
    CompareProcesses.CompareProcPs()

def two():
    CheckProcessesFromPs.CheckProcessesFromPs()

def three():
    BruteForcePids.BruteForcePidsByFork()

def four():
    priority.CheckAll()

def five():
    CheckProcfs.checkDir()

def six():
    kernel_module.KernelModule()

def ten():
    exit()

def switch_demo(argument):
    switcher = {
        '1': one,
        '2': two,
        '3': three,
        '4': four,
        '5': five,
        '6': six,
        '10': ten,
    }
    func=switcher.get(argument,lambda :'Nie ma takiego numeru...')
    return func()

def showMenu():
    print("--------------------------")
    print("1. Porownanie zawartosci katalogu /proc z wynikiem programu ps")
    print("2. Porownanie informacji zebranych z programu ps z informacjami z procfs")
    print("3. Sprawdzenie wyniku programu ps poprzez tworzenie nowych procesow")
    print("4. Porwnanie informacji zebranych z programu ps z informacjami z wywolan systemowych")
    print("5. Sprawdzenie sterownika procfs poprzez sprawdzenie dostepnosci do katalogow procesow w /proc")
    if os.path.exists("Main.ko"):
        if (Helper.checkPermission()):
            print("6. Sprawdzenie podmiany wywolan systemowych poprzez uruchomienie ladowalnego modulu")
        else:
            print("6. Brak uprawnien do uruchomienia ladowalnego modulu")
    else:
        print("6. Ladowalny modul nie znajduje sie w katalogu")

    print("10. Wyjscie")

if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='A tutorial of argparse!')
    parser.add_argument('-a','--Basic', action="store_true", help = "Porownanie zawartosci katalogu /proc z wynikiem programu ps", default=False)
    parser.add_argument('-b','--Basic2',action="store_true", help = "Porownanie informacji zebranych z programu ps z informacjami z procfs", default=False)
    parser.add_argument('-c','--Brute',action="store_true", help = "Sprawdzenie wyniku programu ps poprzez tworzenie nowych procesow", default=False)
    parser.add_argument('-d','--Bas', action="store_true", help = "Sprawdzenie wyniku programu ps poprzez tworzenie nowych procesow", default=False)
    parser.add_argument('-e','--E', action="store_true", help = "Sprawdzenie wyniku programu ps poprzez tworzenie nowych procesow", default=False)
    parser.add_argument('-f','--F', action="store_true", help = "Sprawdzenie podmiany wywolan systemowych poprzez uruchomienie ladowalnego modulu- wymagene uruchomienie przez administratora", default=False)

    args = parser.parse_args()
    print(args)

    if not (len(sys.argv) > 1):
        os.system('clear')
        print("Program wykrywajcy procesy")
        while(1):
            showMenu()
            value = input()
            switch_demo(value)
    else:
        if args.Basic is True:
            switch_demo('1')
        if args.Basic2 is True:
            switch_demo('2')
        if args.Brute is True:
            switch_demo('3')
        if args.Bas is True:
            switch_demo('4')
        if args.E is True:
            switch_demo('5')
        if args.F is True:
            switch_demo('6')
