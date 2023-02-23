# NODEBREACH :: REWRITE
# Terminal module
# Licensed under the MIT license

class port():
    def __init__(num, type, name):
        self.num = num
        self.type = type
        self.name = name
        self.open = False
    def open():
        self.open = True
    def close():
        # probably never gonna be used, but nice to have
        self.open = False



class terminal():
    def __init__(self, name, ip, ports, inviolable, firewall, proxy, trace, logins):
        self.name = name # string
        self.ip = ip # string
        self.ports = ports # list of port() objects
        self.inviolable = inviolable # boolean
        self.firewall = firewall # integer
        self.proxy = proxy # integer
        self.trace = trace # integer
        self.logins = logins # dictionary of strings
    def login(username, password):
        if self.logins[username] == password:
            return True
        else:
            return False
    