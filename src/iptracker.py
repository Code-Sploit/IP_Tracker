import os
import urllib2
import json
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a","--action",dest="action",default="none")
parser.add_option("-i","--input",dest="input",default="none")
(options,args) = parser.parse_args()

from colorama import Fore as colors


def generate():
    from random import randint

    amount = input(str("Amount (Max: 10): "))

    for i in range(0,amount): 
        number1 = str(randint(1,254))
        number2 = str(randint(1,254))
        number3 = str(randint(1,254))
        number4 = str(randint(1,254))
        current_ipv1 = number1 + "." + number2 + "." + number3 + "." + number4
        number5 = str(randint(1,54))
        number6 = str(randint(1,54))
        number7 = str(randint(1,54))
        number8 = str(randint(1,254))
        current_ipv2 = number5 + "." + number6 + "." + number7 + "." + number8
        print(str(i) + current_ipv1)
        print(str(i) + current_ipv2)


def manual():
    while True:
        try:
            ip=raw_input(colors.LIGHTGREEN_EX + "[*] What is your target IP: " + colors.RESET)
            with open("log/history.txt","a") as f:
                f.write("\n")
                f.write(ip)
            url = "http://ip-api.com/json/"
            response = urllib2.urlopen(url + ip)
            data = response.read()
            values = json.loads(data)
            try:
                print("\n")
                print(colors.MAGENTA + " IP: " + colors.CYAN + values['query'])
                print(colors.MAGENTA + " CITY: " + colors.CYAN + values['city'])
                print(colors.MAGENTA + " ISP: " + colors.CYAN + values['isp'])
                print(colors.MAGENTA + " COUNTRY: " + colors.CYAN + values['country'])
                print(colors.MAGENTA + " REGION: " + colors.CYAN + values['region'])
                print(colors.MAGENTA + " TIME ZONE: " + colors.CYAN + values['timezone'])
                print(colors.MAGENTA + " ZIP: " + colors.CYAN + values['zip'])
                print(colors.MAGENTA + " AS: " + colors.CYAN + values['as'])
                print(colors.MAGENTA + " REGION NAME: " + colors.CYAN + values['regionName'] + colors.RESET)
                print("\n")
                choice = raw_input(str(colors.LIGHTYELLOW_EX + "Do you want to log this success? [ Y/y | N/n ] : " + colors.RESET))
                choice = choice.upper()
                if (choice == "Y"):
                    with open("log/log.txt","a") as f:
                        try:
                            f.write("\n")
                            f.write(" IP: " + values['query'] + "\n")
                            f.write(" CITY: " + values['city'] + "\n")
                            f.write(" ISP: " + values['isp'] + "\n")
                            f.write(" COUNTRY: " + values['country'] + "\n")
                            f.write(" REGION: " + values['region'] + "\n")
                            f.write(" TIME ZONE: " + values['timezone'] + "\n")
                            f.write(" ZIP: " + values['zip'] + "\n")
                            f.write(" AS: " + values['as'] + "\n")
                            try:
                                f.write(" REGION NAME: " + values['regionName'] + "\n")
                            except UnicodeEncodeError:
                                pass
                            f.write("\n")
                        except UnicodeEncodeError:
                            pass
                elif (choice == "N"):
                    print(colors.LIGHTGREEN_EX + "Ok!" + colors.RESET)
                else:
                    print(colors.LIGHTRED_EX + "Illegal option!" + colors.RESET)
            except KeyError:
                print(colors.LIGHTRED_EX + "That ip doesn't exists!" + colors.RESET)
                print("\n")
            except KeyboardInterrupt:
                print(colors.LIGHTRED_EX + "\nInterrupt!" + colors.RESET)
                exit()
        except KeyboardInterrupt:
            print(colors.LIGHTRED_EX + "\nInterrupt!" + colors.RESET)
            exit()


def auto():
    from random import randint
    import time

    amount = input(str("Amount: "))

    for i in range(0,amount): 
        number1 = str(randint(1,254))
        number2 = str(randint(1,254))
        number3 = str(randint(1,254))
        number4 = str(randint(1,254))
        current_ipv1 = number1 + "." + number2 + "." + number3 + "." + number4
        number5 = str(randint(1,54))
        number6 = str(randint(1,54))
        number7 = str(randint(1,54))
        number8 = str(randint(1,254))
        current_ipv2 = number5 + "." + number6 + "." + number7 + "." + number8
        try:
            ip=current_ipv1
            with open("log/history.txt","a") as f:
                f.write("\n")
                f.write(ip)
            url = "http://ip-api.com/json/"
            response = urllib2.urlopen(url + ip)
            data = response.read()
            values = json.loads(data)
            try:
                print("\n")
                print(colors.MAGENTA + " IP: " + colors.CYAN + values['query'])
                print(colors.MAGENTA + " CITY: " + colors.CYAN + values['city'])
                print(colors.MAGENTA + " ISP: " + colors.CYAN + values['isp'])
                print(colors.MAGENTA + " COUNTRY: " + colors.CYAN + values['country'])
                print(colors.MAGENTA + " REGION: " + colors.CYAN + values['region'])
                print(colors.MAGENTA + " TIME ZONE: " + colors.CYAN + values['timezone'])
                print(colors.MAGENTA + " ZIP: " + colors.CYAN + values['zip'])
                print(colors.MAGENTA + " AS: " + colors.CYAN + values['as'])
                print(colors.MAGENTA + " REGION NAME: " + colors.CYAN + values['regionName'] + colors.RESET)
                print("\n")
                with open("log/log.txt","a") as f:
                    try:
                        f.write("\n")
                        f.write(" IP: " + values['query'] + "\n")
                        f.write(" CITY: " + values['city'] + "\n")
                        f.write(" ISP: " + values['isp'] + "\n")
                        f.write(" COUNTRY: " + values['country'] + "\n")
                        f.write(" REGION: " + values['region'] + "\n")
                        f.write(" TIME ZONE: " + values['timezone'] + "\n")
                        f.write(" ZIP: " + values['zip'] + "\n")
                        f.write(" AS: " + values['as'] + "\n")
                        f.write(" REGION NAME: " + values['regionName'] + "\n")
                        f.write("\n")
                    except UnicodeEncodeError:
                        pass
            except KeyError:
                print(colors.LIGHTRED_EX + "That ip doesn't exists!" + colors.RESET)
                print("\n")
            except KeyboardInterrupt:
                print(colors.LIGHTRED_EX + "\nInterrupt!" + colors.RESET)
                exit()
        except KeyboardInterrupt:
            print(colors.LIGHTRED_EX + "\nInterrupt!" + colors.RESET)
            exit()

def main():
    if ("none" == options.action):
        print("Please specify an action using the -a flag. OPTS: [ generate | track ].")
        exit()
    try:
        if ("track" == options.action):
            if ("none" == options.input):
                print("Please specify an input type using the -i flag. OPTS: [ manual | auto ].")
                exit()
            if ("manual" == options.input):
                print("Switching to manual")
                manual()
            elif ("auto" == options.input):
                print("Switching to auto")
                auto()
        elif ("generate" == options.action):
            generate()
    except:
        pass

if __name__ == "__main__":
    main()
