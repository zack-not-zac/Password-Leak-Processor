#!/usr/bin/env python
import re
from sys import argv

def open_file(path):
    try:
        f = open(path,"rt")     # Attempts to open file as read only text, prints error if it cannot.
    except Exception as e:
        print("Unable to open file: " + str(e))
        exit()

    print("File opened at " + path + " successfully")
    return f

def get_matches(keyword,data,obfuscate="Y"):
    query="^[\w\-\.]*@("+keyword+"|[\w\.]+"+keyword+")[\w\-]*(\.\w*|\.\w*\.\w*)\:.*$"    # Query for regex emails followed by a pass, i.e test@domain.com:pass, where "domain" is the keyword
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

def save_to_file(matches):
    fn = input("Enter a filename:\n")
    try:
        file=open(fn,"w")
    except:
        print("Unable to open file to save at "+ fn)
        print_set(matches)
    
    for i in matches:
        file.write(i+"\n")
    
    file.close()
    return

def print_set(matches):
    for i in matches:
        print(i)

    return 

def main():
    if len(argv) < 3:
        print("Usage: " + argv[0] + " [file_name] [keyword]")
        exit()
    else:
        file=open_file(str(argv[1]))
    
    kw = str(argv[-1])
    data=convert_file_to_set(file)

    obfuscate_pw = input("Obfuscate passwords? (Y/N) ").upper()
    if obfuscate_pw != "Y" and obfuscate_pw !="N":
        obfuscate_pw="Y"
    matches=get_matches(kw,data,obfuscate_pw)

    save=input("Save output to file? (Y/N) ").upper()
    if save != "Y" and save !="N":
        save="N"

    if save=="Y":
        save_to_file(matches)
    else:
        print_set(matches)


if __name__ == "__main__":
    main()
