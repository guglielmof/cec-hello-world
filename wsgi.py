import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    fh = open("/mnt/hello.txt", "w")
    lines_of_text = ["a line of text", "another line of text", "a third line"]
    fh.writelines(lines_of_text)
    fh.close()
    
    #return "Hello World! Greetings from "+socket.gethostname()+"\n"

    fh = open("/mnt/hello.txt", "r")
    for i in fh:
        s = i
    return s

if __name__ == "__main__":
    application.run()
