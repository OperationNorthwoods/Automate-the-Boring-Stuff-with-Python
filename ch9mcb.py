#!/usr/bin/env python

# adding more functionality to this per ch9 using shelve module. original file: ch6MultiClipboard.py
# not using .pyw file per the instructions as it seems that will only work on windows
# this is a guided project from the book, but I didn't copy and paste the code, and added more features myself

# Usage Guide: python ch9mcb.py save <keyword> - Saves clipboard to the keyword.
#              python ch9mcb.py <keyword> - Loads a keyword's value to the clipboard.
#              python ch9mcb.py list - Loads all keyword's values to the clipboard.
#              python ch9mcb.py clear - Deletes all saved info.
#              python ch9mcb.py delete <keyword> - 

import sys
import pyperclip
import shelve
import pprint

mcbShelf = shelve.open('ch9mcb')

if len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        # list out all saved content, and print the keys and values
        pyperclip.copy(pprint.pformat(list(mcbShelf.values())))
        print('Your list has been copied!')
        print(pprint.pformat(list(mcbShelf.keys())))
        print(pprint.pformat(list(mcbShelf.values())))
    elif sys.argv[1].lower() == 'clear':
        # removes all data from the saved list permenantly
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        # keyword for already existing value, value is copied to clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print('Copied to clipboard.')
    else:
        print('Your keyphrase is not detected!')
        print('Please follow the cmd argument format outlined in the usage guide in Lines 7-10')
elif len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        # saves a new value based on the key entered after save
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print('The keyword you entered has been associated with your clipboard\'s contents.')
    if sys.argv[1].lower() == 'delete':
        # removes a specific key-value pair
        del mcbShelf[sys.argv[2]]
        print(f'the keyword "{sys.argv[2]}" and its assciated value has been deleted.')
    else:
        print('Please follow the cmd argument format outlined in the usage guide in Lines 7-10')
else:
    print('Please follow the cmd argument format outlined in the usage guide in Lines 7-10')

mcbShelf.close()