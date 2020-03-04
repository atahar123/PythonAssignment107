# SIMPLEST - Restaurant Waiter Helper

# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# DOD
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!
# has documentation
# follows best practices

# starter code
menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']
food_order = []
print(menu)

cusorder = []
maxLengthList = 3
while len(cusorder) < maxLengthList:
    item = input('Please select what you want from the menu ')
    cusorder.append(item)
    print(cusorder, '\n')

print(f'Your final order is {cusorder}')

# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
#  print everything