import pyperclip
import re

py = pyperclip

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                      # area code
(\s|-|\.)                               # seperator
(\d{3})                                 # first 3 digits
(\s|-|\.)                               # seperator
(\d{4})                                 # last 4
(\s*(ext|x|ex|ext.|ex.)\s*(\d{1,5}))?   # extension
)''', re.VERBOSE)

work = py.paste()
res = phoneRegex.search(work)

print(res.group())
