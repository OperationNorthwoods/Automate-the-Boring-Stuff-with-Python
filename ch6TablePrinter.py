tableData = [['apples', 'blueberries', 'grapes', 'blackberries'],
             ['chicken', 'bacon', 'turkey', 'steak'],
             ['avacado', 'pistachio', 'peanut', 'oatmeal']]

justify_char = [0, 0, 0]  # assumses we only have 3 inner lists, could be refactored


# fill in the list with the longest length of any single word in any single list
# this way we know how many characters we will need to justify when printing
def cal_just_amt(list):
    for o in range(len(list)):
        for i in range(len(list[o])):
            if justify_char[o] == 0:
                justify_char[o] = len(list[o][i])
            elif justify_char[o] < len(list[o][i]):
                justify_char[o] = len(list[o][i])


cal_just_amt(tableData)
print(justify_char)

# we have to iterate inner to outer in this function, as we are printing, which goes left to right not top to bottom.
# we are assuming all inner lists have the same len() otherwise this would be more difficult to implment
def print_table(list):
    for i in range(len(list[0])):
        for o in range(len(list)):
            print(list[o][i].rjust(justify_char[o]), end=' ') # , end=' ' makes it format correctly
        print()  # this line makes the format match the book. was messing up with '\n' inside of it b4


print_table(tableData)

# works well
