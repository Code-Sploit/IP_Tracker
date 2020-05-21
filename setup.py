from optparse import OptionParser
from colorama import Fore as colors

parser = OptionParser()
parser.add_option("-a","--action",default="none")

(options,args) = parser.parse_args()

def install():
    import os
    import os.path
    logFileError = ''
    historyFileError = ''
    shortCutFileError = ''
    requiredModulesError = ''
    noErrors = ''
    print(colors.CYAN + "Installing log file..." + colors.RESET)
    if (os.path.isfile("log/log.txt")):
        logFileError = True
        print(colors.RED + "Error: Log file already exists!" + colors.RESET)
        noErrors = False
    else:
        os.system("touch log/log.txt")
        noErrors = True
    print(colors.LIGHTYELLOW_EX + "Done installing log file..." + colors.RESET)
    print(colors.CYAN + "Installing history file..." + colors.RESET)
    if (os.path.isfile("log/history.txt")):
        historyFileError = True
        print(colors.RED + "Error: History file already exists!" + colors.RESET)
        noErrors = False
    else:
        os.system("touch log/history.txt")
        noErrors = True
    print(colors.LIGHTYELLOW_EX + "Done installing log file..." + colors.RESET)
    print(colors.CYAN + "Generating shortcut execution file..." + colors.RESET)
    if (os.path.isfile("tracker.py")):
        shortCutFileError = True
        print(colors.RED + "Shortcut file already exists!" + colors.RESET)
        noErrors = False
    else:
        os.system("cp src/iptracker.py tracker.py")
        print(colors.CYAN + "Generating shortcut execution file..." + colors.RESET)
    print(colors.LIGHTYELLOW_EX + "Done generation shortcut execution file..." + colors.RESET)
    print(colors.CYAN + "Installing required modules..." + colors.RESET)
    if (os.path.isfile("/usr/bin/pip") or os.path.isfile("/usr/bin/pip2") or os.path.isfile("/usr/bin/pip2.6") or os.path.isfile("/usr/bin/pip2.7")):
        os.system("pip install -r lib/requirements.txt")
        print(colors.LIGHTYELLOW_EX + "Done installing required modules..." + colors.RESET)
        noErrors = True
    else:
        print(colors.LIGHTRED_EX + "Failed to install required modules..." + colors.RESET)
        requiredModulesError = True
        noErrors = False
        print(colors.LIGHTRED_EX + "Is pip2 installed" + colors.RESET)
        print(colors.LIGHTYELLOW_EX + "Done installing required modules..." + colors.RESET)
    
    print(colors.LIGHTYELLOW_EX + "Done installing" + colors.RESET)
    print("\n\n"  + colors.LIGHTRED_EX + "Errors: ")
    if (logFileError == True):
        print("\n   " + colors.LIGHTRED_EX + "logFileError returned error code (1). Desc: Log file already exists!")
    if (historyFileError == True):
        print("\n   " + colors.LIGHTRED_EX + "historyFileError returned error code (1). Desc: History file already exists!")
    if (shortCutFileError == True):
        print("\n   " + colors.LIGHTRED_EX + "shortCutFileError returned error code (1). Desc: Shortcut already exists!")
    if (requiredModulesError == True):
        print("\n   " + colors.LIGHTRED_EX + "requiredModulesError returned error code (1). Desc: Could not install required modules because of pip version!\n\n")
    if (noErrors == True):
        print("\n   " + colors.GREEN + "None!")


def remove():
    import os
    import os.path
    print("Removing log file...")
    os.system("rm log/log.txt")
    print("Done removing log file...")
    print("Removing history file...")
    os.system("rm log/history.txt")
    print("Done removing log file...")
    print("Degenerating shortcut execution file...")
    os.system("rm tracker.py")
    print("Done degenerating shortcut execution file...")
    print("Removing required modules...")
    if (os.path.isfile("/usr/bin/pip") or os.path.isfile("/usr/bin/pip2") or os.path.isfile("/usr/bin/pip2.6") or os.path.isfile("/usr/bin/pip2.7")):
        os.system("pip uninstall -r lib/requirements.txt")
        print("Done Removing required modules...")
    else:
        print("Failed to Remove required modules...")
        ftirm = True
        print("Is pip2 installed")
    
    print("Done Removing")
    if (ftirm == True):
        print("There were errors processing the removal of the required modules...")
        print("The modules may still be installed!")
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
    elif ("remove" in options.action):
        remove()
    else:
        print("Illegal option!")
        print("Exited!")
        exit(1)

if __name__ == "__main__":
    main()
