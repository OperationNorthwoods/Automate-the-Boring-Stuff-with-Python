# Date Detection proj
import re

dateRegex = re.compile(r'([0-1][0-9])/([0-3][0-9])/([1-2][0-9][0-9][0-9])')

# main user input loop
while True:
    user_input = input('Please enter a date in the format MM/DD/YYYY: ')
    date = dateRegex.search(user_input)
    # print('Date: ' + str(date) + '\n' + 'Input: ' + str(dateRegex.search(input)) + '\n'+'Groups: ' + str(date.groups()) + '\n'+'Group: ' + str(date.group(0)))
    if date:
        print('Entered data test: ' + str(date.group(0)))
        month = date.group(1)
        day = date.group(2)
        year = date.group(3)
        print(str(month)+' '+str(day)+' '+str(year))
        break
    else:
        print('Please Enter a Date in the proper format!')
        continue

# works well

