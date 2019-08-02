import json
import os

import threading as tth
from threading import Thread

import time


class MyThread(tth.Thread):
    def __init__(self, path, value):
        Thread.__init__(self)
        self.path = path
        self.value = value

    def run(self):
        with open(self.path, 'w') as f:
            json.dump(self.value, f, indent=2)


class MyJsonParse(object):

    __valueDict = {}

    def set_dict(self):
        with open('input.json', 'r') as f:
            self.__valueDict = json.load(f)

    def make_all(self):

        os.mkdir('write_here')

        for item in self.__valueDict.items():
            os.mkdir('write_here/{}'.format(str(item[0])))
            for value in item[1]:
                with open('write_here/{}/{}.json'.format(item[0], value['id']), 'w') as f1:
                    json.dump(value, f1, indent=2)

    def make_all_thread(self):
        os.mkdir('write_here_tread')
        for item in self.__valueDict.items():
            os.mkdir('write_here_tread/{}'.format(str(item[0])))
            for value in item[1]:
                MyThread('write_here_tread/{}/{}.json'.format(item[0], value['id']), item[1]).start()


new = MyJsonParse()

new.set_dict()

start = time.time()
new.make_all()  # one thread
print(time.time() - start)

start = time.time()
new.make_all_thread()  # multiThread
print(time.time() - start)
