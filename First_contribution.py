from collections.abc import Iterable
import time as t
from datetime import *
from logging import NullHandler
import os
import itertools
import threading
import asyncio


class Samplefunc():

    def __init__(self):
        pass
    
    def generate_combination(self, n, lis=[]):
        a = itertools.combinations(lis,n)
        output = [" ".join(i) for i in a]
        return output

    def flatten_list(self, data_in, ignore_type=(str,bytes)):
        for i in data_in:
            print(i)
            if isinstance(i,Iterable) and not isinstance(i,ignore_type):
               yield from self.flatten_list(i)
            else:
                yield i

    def file_read(self, file_path):
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

    def scenarios(self, dut):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        pid = threading.get_native_id()
        print(f"test is running on {dut} at {current_time} process id is: {pid}")
        t.sleep(5)
        print(f"test is completed on {dut} at {current_time} process id is: {pid}")

    async def say_after(self,delay,what):
            await asyncio.sleep(delay)
            print(what)
    async def sequence_test_run(self,dut):
             start = t.time()
             print(f"started at {t.strftime('%X')} for {dut}")
             task1 = asyncio.create_task(
             self.say_after(2, 'test case started and running on {}'.format(dut)))
             print("test in progress")
             task2 = asyncio.create_task(
             self.say_after(4, 'warning: test is running on {}'.format(dut)))
             await task1
             await task2
             print(f"finished at {t.strftime('%X')}")
             end = t.time()
             total = end - start
             print(f"total time taken for test in seconds {total}")
             
    

    def sequential_exec(self,duts):
        for dut in duts:
             k = dut
             print("test started on {}".format(k))
             asyncio.run(self.sequence_test_run(dut))    
        
    def create_thread(self, duts):
        threads = []
        for dut in duts:
            th = threading.Thread(target = self.scenarios, args = (dut,))
            th.start()
            threads.append(th)
        for th in threads:
            th.join()

obj1 = Samplefunc()
print(obj1.generate_combination(2,[["dut1","dut2","dut3"]]))
obj1.file_read(r"C:\Users\Mohit Ranjan Sahoo\PycharmProjects\all_practice\pyexcel\poems.txt")
print(list(obj1.flatten_list([1,2,3,["hello"],{"name","place"},[23,4,5,6,[1,2,[67,78]]]])))
print(obj1.create_thread(["tanjin101","tanjin114","tanjin105","tanjin109"]))
print(obj1.sequential_exec(["tanjin101","tanjin114","tanjin105","tanjin109"]))

