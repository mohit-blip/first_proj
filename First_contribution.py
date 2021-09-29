from collections.abc import Iterable
from logging import NullHandler
import os
import itertools


class Samplefunc():

    def __init__(self):
        pass
    
    def generate_combination(self, n, lis=[]):
        a = itertools.combinations(lis,n)
        output = [" ".join(i) for i in a]
        return output


    def flatten_list(self,data_in,ignore_type=(str,bytes)):
        for i in data_in:
            print(i)
            if isinstance(i,Iterable) and not isinstance(i,ignore_type):
               yield from self.flatten_list(i)
            else:
                yield i

    def file_read(self,file_path):
        flag = 0
        if os.path.isfile(file_path) == True:
            file = open(file_path, "r")
            content = file.read()
            print("lets read the file")
            print(content)
            pre_line = content.split("\n")
            for i in pre_line:
                if i:
                    flag = flag + 1
            print("lines in the file = {}".format(flag))
            file.seek(0)
            d = {}
            for newline in file:
                newline = newline.strip()
                newline = newline.lower()
                words = newline.split(" ")
                for word in words:
                   if word in d:
                     d[word] = d[word] + 1
                   else:
                     d[word] = 1
            for oc in d.keys():
               print("the \"{}\" have = {} occurances".format(oc, d[oc]))
            file.close()
        else:
           try:
              file = open(file_path, "w")
              file.write("12345")
              if os.path.exists(file_path) == True:
                print("file created successfully")
                file.close()
           except Exception as e:
                print("couldn't create file because of {}, do the needful".format(e))
     
    

obj1 = Samplefunc()
print(obj1.generate_combination(2,["jan","feb","march","april"]))
obj1.file_read(r"C:\Users\Mohit Ranjan Sahoo\PycharmProjects\all_practice\pyexcel\poems.txt")
print(list(obj1.flatten_list([1,2,3,["hello"],{"name","place"},[23,4,5,6,[1,2,[67,78]]]])))

