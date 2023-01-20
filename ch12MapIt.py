# a program which takes a command line argument or contents of the clipboard 
# and opens a google maps link to that page

import webbrowser
import pyperclip
import sys

if len(sys.argv) > 2:
    print('Getting Address from Command Line Argument...')
    fromCmdArg = ' '.join(sys.argv[1:])
    print(f'opening this address in Google Maps: {fromCmdArg}')
    webbrowser.open('https://www.google.com/maps/place/'+fromCmdArg)
if len(sys.argv) == 1:
    print('Getting Address from Clipboard...')
    fromClipboard = pyperclip.paste()
    print(f'opening this address in Google Maps: {fromClipboard}')
    print(fromClipboard)
    webbrowser.open('https://www.google.com/maps/place/'+fromClipboard)
