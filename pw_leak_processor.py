#!/usr/bin/env python

import re
from sys import argv

def open_file(path):
    try:
        f = open(path,"rt")     # Attempts to open file as read only text, prints error if it cannot.
    except Exception as e:
        print("Unable to open file: " + str(e))
        exit()
    return f

def get_matches(keyword,data,obfuscate="Y"):
    query="^[\w\-\.]*@" + keyword + "[\w\-]*\.\w*\:.*$"     # Query for regex emails followed by a pass, i.e test@domain.com:pass, where "domain" is the keyword
    matches=set()
    for line in data:
        result=re.search(query,line)
        try:
            s = result.string
            if obfuscate=="Y":
                s = re.sub("(?<=\:\w).*(?=\w)","********",s)    # Obfuscates the passwords printed, for use in support tickets.
            
            matches.add(s)
        except AttributeError:
            pass
    
    return matches


def convert_file_to_set(file):
    s = set()
    for line in file:
        line=line.rstrip() # Remove newline chars
        s.add(line)
    
    return s
        

def main():
    if len(argv) < 2:
        print("Usage: " + argv[0] + " [file_name]")
        exit()
    else:
        file=open_file(str(argv[1]))
    
    kw = input("Enter a domain (or part of a domain such as a company name) to search for: ")
    data=convert_file_to_set(file)

    obfuscate_pw = input("Obfuscate passwords? (Y/N) ").upper()
    if obfuscate_pw != "Y" and obfuscate_pw !="N":
        obfuscate_pw="Y"
    matches=get_matches(kw,data,obfuscate_pw)

    for i in matches:
        print(i)


if __name__ == "__main__":
    main()
