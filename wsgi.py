import socket
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    fh = open("/mnt/hello.txt", "a")
    lines_of_text = ""+socket.gethostname()+": "+time.time()+"\n"
    fh.writelines(lines_of_text)
    fh.close()
    
    #return "Hello World! Greetings from "+socket.gethostname()+"\n"

    fh = open("/mnt/hello.txt", "r")
    s =""
    for i in fh:
        s += i
    return s

if __name__ == "__main__":
    application.run()
