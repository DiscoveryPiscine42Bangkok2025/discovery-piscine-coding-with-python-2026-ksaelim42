#!/usr/bin/python3
import sys, re


try:
    if len(sys.argv)!= 3:
        print("none")
    else:
        print(len(re.findall(sys.argv[1], sys.argv[2])))
            
except:
    print("Error")