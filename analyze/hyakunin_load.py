import sys
import threading


class Chihayahuru(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        file_load = open('../input/hyakunin.txt', 'r', encoding='UTF-8')
        data = file_load.readlines()
        file_load.close()

        line: str
        for line in data:
            arg_sys = sys.argv
            match_word = arg_sys[1]
            if line.find(match_word) < 0:
                continue
            output = line[:-1]
            print(output)


thread = Chihayahuru()
thread.run()
