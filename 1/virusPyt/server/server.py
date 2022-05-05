import random
from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 14880))


def new(string : str):
    try:
        path : str = str(random.randint(0, 1000000) + random.randint(0, 1000000))+ ".txt"
        with open(path, "w") as file: file.write(string)
        return True
    except: return False


def arbeiten():
    return("Ja Sire")

print ("Ist bereit, Sire")
server.register_function(new)
server.register_function(arbeiten)
server.serve_forever()
