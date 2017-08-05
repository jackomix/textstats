import re, colorama, sys, pip
from colorama import Fore, Back, Style, init
init()
init(autoreset=True)
installed_packages = pip.get_installed_distributions()
flat_installed_packages = [package.project_name for package in installed_packages]

print("Checking if py-getch is installed.")
if not 'py-getch' in flat_installed_packages:
    print("Found that py-getch is not installed.")
    print("Starting to install py-getch.")
    pip.main(['install', py-getch])
    print("Done installing py-getch.")

def printstats(text, string):
    print(Style.BRIGHT + Fore.GREEN + text, Style.BRIGHT + Fore.WHITE + string)

print("Starting program...")
from getch import getch, pause
while True:
    sys.stderr.write("\x1b[2J\x1b[H")

    string = input("Please type in something... ")
    print("Set string, string to ", string, ".", sep="")

    stringreverse = string[::-1]
    print("Reversed string.")

    stringletters = str(len(re.sub("[^a-zA-Z]+", "", string).lower()))
    print("Got number of letters.")

    stringlength = str(len(string))
    print("Got length of string.")

    palimdrone = "No"
    if re.sub("[^a-zA-Z]+", "", string).lower() == re.sub("[^a-zA-Z]+", "", stringreverse).lower(): palimdrone = "Yes"
    print("Set palimdrone variable.")

    vowelsvar = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
    vowels = (str(vowelsvar))
    print("Got number of vowels.")

    stringlower = string.lower()
    print("Lowercased string.")

    stringupper = string.upper()
    print("Uppercased string.")

    consonantsvar = len(re.sub("[^a-zA-Z]+", "", string).lower()) - vowelsvar
    consonants = str(consonantsvar)
    print("Got number of consonants.")

    stringnumbers = str(len(re.sub("[^0-9]+", "", string).lower()))
    print("Got number of numbers.")

    stringwords = str(len(string.split()))
    print("Got number of words.")

    stringlowernum = str(len(re.findall(r'[a-z]',string)))
    print("Got number of lowercase characters.")

    stringuppernum = str(len(re.findall(r'[A-Z]',string)))
    print("Got number of uppercase characters.")

    print("Going to print stats.")
    sys.stderr.write("\x1b[2J\x1b[H")
    print(Style.BRIGHT + Fore.GREEN + "===", Style.BRIGHT + Fore.WHITE + 'Stats of "', Style.BRIGHT + Fore.WHITE + string, Style.BRIGHT + Fore.WHITE + '"', Style.BRIGHT + Fore.GREEN + "===", sep="")
    printstats("String:", string)
    printstats("Reversed:", stringreverse)
    printstats("Palimdrone:", palimdrone)
    printstats("Words:", stringwords)
    printstats("Characters:", stringlength)
    printstats("Numbers:", stringnumbers)
    printstats("Letters:", stringletters)
    printstats("Vowels:", vowels)
    printstats("Consonants:", consonants)
    printstats("Uppercase characters:", stringuppernum)
    printstats("Lowercase characters:", stringlowernum)
    printstats("Lowercased:", stringlower)
    printstats("Uppercased:", stringupper)
    pause("")
