# coin flip streaks

import random
import copy

tenK_List = []
generated_list = []
numberOfStreaks = 0

for y in range(10000):
    streak_counter = 0
    streak_letter = ''
    # Code that creates a list of 100 'heads' and 'tails' values.
    for x in range(100):
        counter = x
        if random.randint(0, 1) == 0:
            generated_list.append('H')
        else:
            generated_list.append('T')
        if counter == 99:
            tenK_List.append(generated_list.copy())
            generated_list = []
    # Code that checks if there is a streak of 6 'heads' or 6 'tails' in a row.
    for x in range(100):
        if x == 0:
            # runs on 1st iteration only, sets initial letter for streak checking
            # outer list index is y ; inner list index is x
            streak_letter = tenK_List[y][x]   # see line 27 comment
        # checks if the initial streak letter is the same as the next one
        if streak_letter == tenK_List[y][x]:  # see line 27 comment
            streak_counter += 1
            if streak_counter == 6:  # reset streak after it hits 6
                # print('STREAKKKK!!!!!!!!!')
                numberOfStreaks += 1
                streak_counter = 0
        else:  # only runs if the letters dont match, sets new streak letter
            streak_counter = 0
            streak_letter = tenK_List[y][x]  # see line 27 comment
        # print(streak_counter, end=' | ')
        # print(streak_letter, end='')

# something is off with this calculation, but this line was copied straight from the book
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
