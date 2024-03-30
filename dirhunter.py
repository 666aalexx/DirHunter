#!/usr/bin/python3

import signal; import argparse; import os; import sys; import requests; import time 

#Colours
redColour = "\033[31m"
greenColour = "\033[32m"
yellowColour = "\033[33m"
blueColour = "\033[34m"
resetColour = "\033[0m"

def sig_handler(sig, frame):
    os.system("clear")
    sys.exit(1)

signal.signal(signal.SIGINT, sig_handler)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")
parser.add_argument("-w", "--wordlist")
args = parser.parse_args()

target = args.target
wordlist = args.wordlist

def start():
    global wordlist
    if target and wordlist:
        if os.path.exists(wordlist):
            wordlist = open(wordlist, "r")
            wordlist = wordlist.read().split("\n")
        else:
            print(f"{redColour}The dictionary does not exist{endColour}")
            sys.exit(1)
        with open("directoriesFound.txt", "a") as output:
            for directories in wordlist:
                url = f"http://{target}/{directories}"
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print(f"{greenColour}[*]{resetColour} Directory found: {url}")
                    output.write(f"{url}\n")

        with open("directoriesFound.txt", "a") as output:
            for directories in wordlist:
                url = f"https://{target}/{directories}"
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print(f"{greenColour}[*]{resetColour} Directory found: {url}")
                    output.write(f"{url}\n")

    else:
        sys.exit(1)

start()
