# mad libs program
# searchs for ["ADJECTIVE", "NOUN", "VERB", "ADVERB"] in a given .txt file
# prompts user for input on each occurance of the above 
# overwrites old text file with each item in the list replaced with user's inputed words
# improvements: generate new file instead of overwriting old one

from pathlib import Path
import re
import os

ADJ = re.compile(r'ADJECTIVE')
ADV = re.compile(r'ADVERB')
VERB = re.compile(r'VERB')
NOUN = re.compile(r'NOUN')

pathy = Path.home()/'Documents'
files = pathy.glob('madlibs[0-9]*.txt')
# print(list(files))
for file in files:
    print(file)
    current_file = ''  # this is the string we do work in before writing it back overtop the original file
    with open(file, 'r') as reader:
        current_file = reader.read()
        # print(current_file)
        current_file = re.sub(ADJ, input('Please enter a new adjective:\n'), current_file)
        current_file = re.sub(ADV, input('Please enter a new adverb:\n'), current_file)
        current_file = re.sub(VERB, input('Please enter a new verb:\n'), current_file)
        current_file = re.sub(NOUN, input('Please enter a new noun:\n'), current_file)
        # print(current_file)
    with open(file, 'w') as writer:
        # overwrite file with changes
        writer.write(current_file)
