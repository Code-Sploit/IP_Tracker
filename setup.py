from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a","--action",default="none")

(options,args) = parser.parse_args()


def importModules():
    import os
    import os.path

def install():
    import os
    import os.path
    print("Installing log file...")
    os.system("touch log/log.txt")
    print("Done installing log file...")
    print("Installing history file...")
    os.system("touch log/history.txt")
    print("Done installing log file...")
    print("Generating shortcut execution file...")
    os.system("cp src/iptracker.py tracker.py")
    print("Done generation shortcut execution file...")
    print("Installing required modules...")
    if (os.path.isfile("/usr/bin/pip") or os.path.isfile("/usr/bin/pip2") or os.path.isfile("/usr/bin/pip2.6") or os.path.isfile("/usr/bin/pip2.7")):
        os.system("pip install -r lib/requirements.txt")
        print("Done installing required modules...")
    else:
        print("Failed to install required modules...")
        ftirm = True
        print("Is pip2 installed")
    
    print("Done installing")
    if (ftirm == True):
        print("There were errors processing the install of the required modules...")
        print("The script [may] not work!")
        exit(1)
    else:
        exit(0)

def clearHistory():
    import os
    import os.path
    if (os.path.isfile("log/history.txt")):
        print("Refreshing log/history.txt...")
        os.system("rm log/history.txt")
        os.system("touch log/history.txt")
        print("Done refreshing log/history.txt...")
    else:
        print("History file does not exists!")
        print("Did you install?")
        exit(1)

def clearLog():
    import os
    import os.path
    if (os.path.isfile("log/log.txt")):
        print("Refreshing log/log.txt...")
        os.system("rm log/log.txt")
        os.system("touch log/log.txt")
        print("Done refreshing log/log.txt...")
    else:
        print("Log file does not exists!")
        print("Did you install?")
        exit(1)

def main():
    if ("none" in options.action):
        print("You must enter an action using the -a flag!")
    elif ("install" in options.action):
        install()
    elif ("clear_history" in options.action):
        clearHistory()
    elif ("clear_log" in options.action):
        clearLog()
    else:
        print("Illegal option!")
        print("Exited!")
        exit(1)

if __name__ == "__main__":
    main()
