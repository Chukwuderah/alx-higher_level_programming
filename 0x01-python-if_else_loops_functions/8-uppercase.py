#!/usr/bin/python3
def uppercase(str):
    for p in str:
        if ord("a") <= ord(p) <= ord("z"):
            p = chr(ord(p) - 32)
        print("{:s}".format(p), end="")
    print()

