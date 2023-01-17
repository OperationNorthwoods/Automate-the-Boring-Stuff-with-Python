# this script renames files in a hard-coded directory (right now it is 'Temp_Backup')
# files with American-style (MM-DD-YYYY) dates will renamed to European-style (DD-MM-YYYY) dates

import shutil
import os
import re
from pathlib import Path

# American-style date regex
datePattern = re.compile(r'''^(.*?)         # any text before the date
((0|1)?\d)-                                 # one or more digits for the month
((0|1|2|3)?\d)-                             # one or two digits for the day
((19|20)\d\d)                               # four digits for the year
(.*?)$                                      # any text after the date
''', re.VERBOSE)

pathToSearch = Path.home()/'Documents'/'Temp_Backup'

fileList = os.listdir(pathToSearch)

for file in fileList:
    # print(file)
    res = datePattern.search(file)
    if res:
        americanFileName = file
        # print('Source: ' + americanFileName)
        beforePart, monthPart, dayPart, yearPart, afterPart = *res.group(1, 2, 4, 6, 8),
        euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
        # print('Dest: '+ euroFileName)
        # print(pathToSearch/americanFileName)
        shutil.move(pathToSearch/americanFileName, pathToSearch/euroFileName)

# worked! I did it my way (frank sinatra voice) and used minimal code from the book
# I've also kept some of the print() lines i used for testing in here, even though they are commented out
# Note: This DOES NOT Work on CWD, only the hard coded dir! 