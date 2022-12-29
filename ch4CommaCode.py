# CommaCode

def commaCode(a_list):
    for x in range(len(a_list)):
        if x != (len(a_list)-1):
            print(a_list[x], end=', ')
        else:
            print('and ' + a_list[x], end='')

spam = ['apples', 'bananas', 'tofu', 'cats']
commaCode(spam)
