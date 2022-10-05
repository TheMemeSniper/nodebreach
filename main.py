import time
import os 
import platform
import random
import getopt
import playsound
import importlib.util
import sys

# FUNCTIONS START

def probe():
    print("Probing system...")
    if os.path.exists("terminals/"+currentip+"/manifest.txt"):
        manifestlines = open("terminals/"+currentip+"/manifest.txt","r")
        manifest = manifestlines.readlines()
        print(manifest)
        print("/terminals/"+currentip+"/manifest.txt")
        print("Ports required for crack: "+manifest[0])
        if manifest[14] == "1\n":
            print("INVIOBILITY DETECTED")
        if manifest[10] == "1\n":
            print("Active proxy detected")
        if manifest[12] == "1\n":
            print("Active firewall detected")
        if manifest[1] == "1\n":
            print("SMTP Port - 25")
        if manifest[2] == "1\n":
            print("FTP Port - 21")
        if manifest[3] == "1\n":
            print("HTTP Webserver Port - 80")
        if manifest[4] == "1\n":
            print("SSH Port - 22")
        if manifest[5] == "1\n":
            print("KBT Medical Services - 104")
        if manifest[6] == "1\n":
            print("Torrent Port - 6881")
        if manifest[7] == "1\n":
            print("HTTP SSL Port - 443")
        if manifest[8] == "1\n":
            print("Pacific Port - 19")
        if manifest[9] == "1\n":
            print("RTSP Port - 554")
    else:
        print("Probe failed!")

def contract():
    print("Contract Database")
    ccontracttxt = open("contracts/current.txt")
    mod_string = str(ccontracttxt.read())[:len(ccontracttxt.read()) - 1]
    ccmanifest = open("contracts/"+mod_string+"/manifest.txt")
    lines = ccmanifest.readlines()
    for line in lines:
        print(line)
    spec = importlib.util.spec_from_file_location("cond.py", "contracts/"+mod_string+"/cond.py")
    foo = importlib.util.module_from_spec(spec)
    sys.modules["cond.py"] = foo
    spec.loader.exec_module(foo)
    if foo.go() == True:
        cf = open("contracts/current.txt","w")
        ncf = int(mod_string)
        cf.write((ncf + 1))
        print('Contract completed, run "contracts" again for your next contract')
    else:
        print("Contract not complete")
        
    

def generateip():
    ip1 = random.randint(1,255)
    if dbm == 1:
        dbo.write("ip1 = "+ip1)
    ip2 = random.randint(1,255)
    if dbm == 1:
        dbo.write("ip2 = "+ip2)
    ip3 = random.randint(1,255)
    if dbm == 1:
        dbo.write("ip3 = "+ip3)
    ip4 = random.randint(1,255)
    if dbm == 1:
        dbo.write("ip4 = "+ip4)
    return str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)


def help():
    print("Nodebreach Terminal Help")
    print("")
    print("help - Displays this list")
    print("")
    print("contracts - Displays your contracts")
    print("")
    print("quit - Quit Nodebreach")
    print("")
    print("connect - Connect to a remote terminal")
    print("")
    print("clear - Clear terminal screen")
    print("")
    print("dc/disconnect - Disconnect from a remote terminal")
    print("")
    print("portbreach - Gain admin access to remote terminal through ports")
    print("")
    print("probe - Inspect security on a remote terminal")

def clearterminal():
    if osp == "win":
        os.system('cls')
    else:
        os.system('clear')

def about():
    print("███    ██  ██████  ██████  ███████ ██████  ██████  ███████  █████   ██████ ██   ██")
    print("████   ██ ██    ██ ██   ██ ██      ██   ██ ██   ██ ██      ██   ██ ██      ██   ██")
    print("██ ██  ██ ██    ██ ██   ██ █████   ██████  ██████  █████   ███████ ██      ███████")
    print("██  ██ ██ ██    ██ ██   ██ ██      ██   ██ ██   ██ ██      ██   ██ ██      ██   ██")
    print("██   ████  ██████  ██████  ███████ ██████  ██   ██ ███████ ██   ██  ██████ ██   ██")
    print('A terminal game about "hacking" people')
    print("Inspired by Hacknet")
    print("Made by TheMemeSniper")
    print("Version info:")
    print("Version 1.0.0")
    print("Branch: Development")

# FUNCTIONS END

dbm = 0

# check user os so we can clear the terminal window correctly
if platform.system_alias == "Windows":
    osp = "win"
else:
    osp = "linux"

clearterminal()

# check for debug argument
if getopt.getopt("debug","debug") == "([], 'debug')":
    print("Debug mode enabled!")
    print("Writing all actions to debug.txt...")
    dbm = 1
    dbo = open("debug.txt", "x")
    dbo.write("// Game started")
print("███    ██  ██████  ██████  ███████ ██████  ██████  ███████  █████   ██████ ██   ██")
print("████   ██ ██    ██ ██   ██ ██      ██   ██ ██   ██ ██      ██   ██ ██      ██   ██")
print("██ ██  ██ ██    ██ ██   ██ █████   ██████  ██████  █████   ███████ ██      ███████")
print("██  ██ ██ ██    ██ ██   ██ ██      ██   ██ ██   ██ ██      ██   ██ ██      ██   ██")
print("██   ████  ██████  ██████  ███████ ██████  ██   ██ ███████ ██   ██  ██████ ██   ██")
print('A terminal game about "hacking" people')
print("Inspired by Hacknet")
print("Made by TheMemeSniper")
print("")
print("")
print("Generating your IP...")


    # pick a random ip for the player and add it to the list
if dbm == 1:
    dbo.write("Generating player IP address...")
playerip = generateip()
if dbm == 1:
        dbo.write("playerip = "+playerip)
print("Your IP address is " +playerip)
print("You have a new contract")
print('Type "contracts" to access it')
print("")
print('View a list of available commands with "help"')
currentip = playerip
# main command line loop
playsound.playsound('assets/music/maintheme.mp3', False)
while True:
    ci = input(currentip+"> ")
    if ci == "contracts":
        contract()
    elif ci == "help":
        help()
    elif ci == "quit":
        print("Quitting Nodebreach...")
        quit()
    elif ci == "connect":
        cnip = input("connect: ")
        if os.path.exists("terminals/"+cnip):
            print("Connected to "+cnip)
            currentip = cnip
        else:
            print("\a")
            print("connect: "+cnip+" not found")
    elif ci == "clear":
        clearterminal()
    elif (ci == "dc") or (ci == "disconnect"):
        if currentip == playerip :
            print("Can't disconnect from your own terminal")
        else:
            print("Disconnected from "+currentip)
            currentip = playerip
    elif ci == "about":
        about()
    elif ci == "probe":
        probe()
    else:
        print("\a")
        print("-bash: "+ci+": command not found")