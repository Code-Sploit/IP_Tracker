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
    backupError = ''
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
    print(colors.LIGHTYELLOW_EX + "Moving src out of backup..." + colors.RESET)
    if (os.path.isfile("lib/backup/src.zip") == True):
        os.system("mv lib/backup/src.zip src/")
        os.system("unzip src/src.zip")
        os.system("rm src/src.zip")
        os.system("mv src/iptracker src/iptracker.py")
        os.system("mv lib/backup/iptracker src/iptracker.py")
    else:
        print(colors.LIGHTYELLOW_EX + "Warning: Could not find the backup of main-src file")
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
    logFileError = ''
    historyFileError = ''
    shortCutFileError = ''
    requiredModulesError = ''
    noErrors = ''
    backupError = ''
    print(colors.CYAN + "Removing log file..." + colors.RESET)
    if (os.path.isfile("log/log.txt") == False):
        noErrors = False
        print(colors.RED + "Error: Log file don't exists!" + colors.RESET)
        logFileError = True
    else:
        os.system("rm log/log.txt")
        noErrors = True
    print(colors.LIGHTYELLOW_EX + "Done Removing log file..." + colors.RESET)
    print(colors.CYAN + "Removing history file..." + colors.RESET)
    if (os.path.isfile("log/history.txt") == False):
        historyFileError = True
        print(colors.RED + "Error: History file don't exists!" + colors.RESET)
        noErrors = False
    else:
        os.system("rm log/history.txt")
        noErrors = True
    print(colors.LIGHTYELLOW_EX + "Done removing log file..." + colors.RESET)
    print(colors.CYAN + "Degenerating shortcut execution file..." + colors.RESET)
    if (os.path.isfile("tracker.py") == False):
        shortCutFileError = True
        print(colors.RED + "Shortcut file don't exists!" + colors.RESET)
        noErrors = False
    else:
        os.system("rm tracker.py")
    print(colors.LIGHTYELLOW_EX + "Done degenerating shortcut execution file..." + colors.RESET)
    print(colors.LIGHTYELLOW_EX + "Creating backup of src script..." + colors.RESET)
    if (os.path.isfile("src/iptracker.py") == True):
        os.system("mv src/iptracker.py lib/backup/iptracker")
        os.system("zip lib/backup/src.zip lib/backup/iptracker")
        os.system("rm lib/backup/iptracker")
        noErrors = True
    else:
        backupError = True
        print(colors.LIGHTRED_EX + "E: main-src-script does'nt exists!")
        print(colors.LIGHTRED_EX + "E: did you remove or backup it?")
        print(colors.LIGHTRED_EX + "E: if you did then do 'python setup.py -a install'!")
    print(colors.LIGHTYELLOW_EX + "Done installing backup of src script..." + colors.RESET)
    print(colors.CYAN + "Removing required modules..." + colors.RESET)
    if (os.path.isfile("/usr/bin/pip") or os.path.isfile("/usr/bin/pip2") or os.path.isfile("/usr/bin/pip2.6") or os.path.isfile("/usr/bin/pip2.7")):
        os.system("pip uninstall -r lib/requirements.txt")
        print(colors.LIGHTYELLOW_EX + "Done removing required modules..." + colors.RESET)
        noErrors = True
    else:
        print(colors.LIGHTRED_EX + "Failed to remove required modules..." + colors.RESET)
        requiredModulesError = True
        noErrors = False
        print(colors.LIGHTRED_EX + "Is pip2 installed" + colors.RESET)
        print(colors.LIGHTYELLOW_EX + "Done removing required modules..." + colors.RESET)
    
    print(colors.LIGHTYELLOW_EX + "Done removing" + colors.RESET)
    print("\n\n"  + colors.LIGHTRED_EX + "Errors: ")
    if (logFileError == True):
        print("\n   " + colors.LIGHTRED_EX + "logFileError returned error code (1). Desc: Log file don't exists!")
    if (historyFileError == True):
        print("\n   " + colors.LIGHTRED_EX + "historyFileError returned error code (1). Desc: History file don't exists!")
    if (shortCutFileError == True):
        print("\n   " + colors.LIGHTRED_EX + "shortCutFileError returned error code (1). Desc: Shortcut don't exists!")
    if (backupError == True):
        print("\n   " + colors.LIGHTRED_EX + "backupError returned error code (1). Desc: main-src-file don't exists!")
    if (requiredModulesError == True):
        print("\n   " + colors.LIGHTRED_EX + "requiredModulesError returned error code (1). Desc: Could not remove required modules because of pip version!\n\n")
    if (noErrors == True):
        print("\n   " + colors.GREEN + "None!")


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

def viewLog():
    with open("log/log.txt","r") as f:
        print("Log:\n\n")
        print(f.read())

def viewHistory():
    with open("log/history.txt","r") as f:
        print("History:\n\n")
        print(f.read())


def main():
    if ("none" == options.action):
        print("You must enter an action using the -a flag!")
    elif ("install" == options.action):
        install()
    elif ("clear_history" == options.action):
        clearHistory()
    elif ("clear_log" == options.action):
        clearLog()
    elif ("remove" == options.action):
        remove()
    elif ("view_log" == options.action):
        viewLog()
    elif ("view_history" == options.action):
        viewHistory()
    else:
        print("Illegal option!")
        print("Exited!")
        exit(1)

if __name__ == "__main__":
    main()
