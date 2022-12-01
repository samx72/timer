import time
import os
from termcolor import colored
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Timer")

os.system("cls")

print(colored("https://github.com/samx72", "green"))
time.sleep(2.5)

os.system("cls")

y_n = input("do you want start this program?(y/n): ")


if(y_n == "n"):
    exit()


if (y_n == "y"):
    os.system("cls")
    print(colored("loading.", "cyan"))
    time.sleep(1)
    os.system("cls")
    print(colored("loading..", "cyan"))
    time.sleep(1)
    os.system("cls")
    print(colored("loading...", "cyan"))
    time.sleep(1)
    os.system("cls")
    print(colored("loaded", "yellow"))
    time.sleep(1)
    os.system("cls")




    h = 0
    m = 0
    s = 0

    while (True):
        time.sleep(1)
        os.system("cls")
        s = s + 1

        if (s == 60):
            m = m + 1
    
        if (m == 60):
            h = h + 1

        print(f"Timer: {h}h, {m}min, {s}sec")
