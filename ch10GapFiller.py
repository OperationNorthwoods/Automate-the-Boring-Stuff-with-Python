# finds gap in numbered files in hard-coded directory and changes file names to eliminate gap

import os
from pathlib import Path
import shutil

quiz = 'Quiz'
answer = 'Answer'
files = os.listdir(quiz)
num = 1

for file in sorted(files):
    if file == 'Answers':
        continue
    if file.endswith(str(num)+'.txt'):
        print('No gap in this file: '+file+' File Number: '+str(num))
    else:
        print('GAP in file: '+file+'Num: '+str(num)+' Fixing...')
        src = os.path.abspath(quiz + '/' + file)
        base_file_name = file.split(".")[0]
        new_file_name = base_file_name[:-4] + str(num).zfill(4) + '.txt'
        dst = os.path.abspath(quiz + '/' + new_file_name)
        shutil.move(src, dst)

    num += 1

# works, detects name change and fixes it. had a little help on this one, lines 19 - 23 were the hardest.