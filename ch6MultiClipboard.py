#!/usr/bin/env python

import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sory, can we do this later this week or maybe next week?""",
        'upsell': """Would you consider making this a monthly donation"""}


# exit the program if 0 or more that 1 cmd line args entered

# if len(sys.argv) != 2:
#     print(f"Use this format\"scriptname.py [keyphrase]\". Only 1 argument is accepted.")
#     sys.exit()

# keyphrase = sys.argv[1]
# ^^^^ old code above ^^^^

try:
    _, keyphrase = sys.argv
except:
    print(f"Use this format\"scriptname.py [keyphrase]\". Only 1 argument is accepted.")
    sys.exit()
# refactored with multiple assignment trick learned from https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/

if keyphrase in TEXT:
    print('Copied to clipboard.')
    pyperclip.copy(TEXT[keyphrase])
else:
    print(f'Your keyphrase is not detected!')
    cont = input("Would you like to enter this keyphrase in the table? (Y/N): ")
    if cont.lower() == 'y':
        new_key = keyphrase
        new_value = input("Enter the value associated with the previously entered keyphrase: ")
        TEXT[new_key] = new_value
        print(TEXT)
    else:
        sys.exit()

# works well. no way to perma save to TEXT from the input, but this was a good lesson in command line args
# next step would be getting short and long flags working for a serious program ie: '-h or -help' doing the same
