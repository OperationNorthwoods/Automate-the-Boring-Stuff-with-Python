import pyperclip as py
import re

# Phone Number and Email extractor
# Guided project from the book

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                      # area code (optional)
(\s|-|\.)                               # seperator
(\d{3})                                 # first 3 digits
(\s|-|\.)                               # seperator
(\d{4})                                 # last 4
(\s*(ext|x|ex|ext.|ex.)\s*(\d{1,5}))?   # extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+                       # username
@                                       # @ symbol
[a-zA-Z0-9.-]+                          # domain name
(\.[a-zA-Z]{2,4})                       # dot-something
)''', re.VERBOSE)

text = str(py.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    py.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found!')

# code from book, very helpful to learn more about processing regex data and how it interacts w/ clipboard