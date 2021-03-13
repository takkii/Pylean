import sys

file_load = open('../input/hyakunin.txt', 'r', encoding='UTF-8')
data = file_load.readlines()
file_load.close()

line: str
for line in data:
    arg_sys = sys.argv
    match_word = arg_sys[1]
    if line.find(match_word) < 0:
        continue
    print(line[:-1])
