from collections.abc import Iterable
import os
import time
import unittest
import itertools

def generate_combination(n,lis=["jan","feb","march","april","may"]):
    a = itertools.combinations(lis,n)
    output = [" ".join(i) for i in a]
    return output


def flatten_list(data_in,ignore_type=(str,bytes)):
    for i in data_in:
        if isinstance(i,Iterable) and not isinstance(i,ignore_type):
            yield from flatten_list(i)
        else:
            yield i
print(list(flatten_list()))

def file_read(file_path):
    if os.path.isfile(file_path) == True:
        file = open(file_path,"r")
        content = file.read()
        print("lets read the file")
        print(content)
        pre_line = content.split("\n")
        for i in pre_line:
            if i:
                flag = flag +1
        print("lines in the file = {}".format(flag))
        d = {}
        for newline in file:
            newline = newline.strip()
            newline = newline.lower()
            words = newline.split(" ")
            for word in words:
                if word in d:
                    d[word] = d[word]+1
                else:
                    d[word] = 1
        for oc in d.keys():
            print("the {} have {} occurances".format(oc,d[oc]))
    else:
        try:
          file = open(file_path,"w")
          file.write("12345")
          if os.path.exists(file_path) == True:
              print("file created successfully")
        except Exception as e:
            print("couldn't create file because of {}, do the needful".format(e))