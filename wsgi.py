import socket
import time
import datetime
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    fh = open("/mnt/logfile.txt", "a")
    lines_of_text = ""+socket.gethostname()+": "+st
    fh.writelines(lines_of_text)
    fh.close()

    #return "Hello World! Greetings from "+socket.gethostname()+"\n"

    fh = open("/mnt/logfile.txt", "r")
    s =""
    for i in fh:
        s += (i+"<br>")
    fh.close()
    return "<p style='color:red; font-size:20px'>Hello World! Greetings from "+socket.gethostname()+"</p>"+s

if __name__ == "__main__":
    application.run()
