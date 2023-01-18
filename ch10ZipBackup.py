# a function which takes a specified hard-coded folder as an argument
# backs up said folder to a zip folder. Increments the folder name with each backup.
# creates backup in same folder your script resides in
# Hint: use Path.home()/'the'/'folder'/'you'/'want' as an argument, it will work fine.
# guided project from book

from pathlib import Path
import os
import zipfile


def backupToZip(folder):

    folder = os.path.abspath(folder) # make sure argument folder path is absolute 

    # figure out what file name should be based on what already exists 
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_backup_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1
    # create the zip file
    print(f'creating {zipFileName}')
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # walk the entire folder tree and compress the files into each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding Files in {foldername}...')
        # add the current folder to the ZIP file
        backupZip.write(foldername)

        # add all the files in this folder to the ZIP file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_backup_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # dont backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


backupToZip(Path.home()/'Documents'/'For_Backup')