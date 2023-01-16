# using a user supplied regex expression, searchs through all text files in the documents folder 
# matching that expresion and prints results

import re
from pathlib import Path

pathy = Path.home()/'Documents'
files = pathy.glob('*.txt')
regie = input('Please Enter your Regex. Only type what would occur between the r" ": ')
find = re.compile(fr'{regie}')
results = []
for file in files:
    print(file)
    current_file = ''
    with open (file, 'r') as reader:
        current_file = reader.read()
        res = re.findall(find, current_file)
        if res == []: # this only seems to work if there are no results at all
            print('Nothing found!')
        else:
            print(res)