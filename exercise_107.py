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
menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras'.title()]
food_order = []
print(menu)
print('1', '-' ,menu[0].capitalize())
print('1', '-' ,menu[1].capitalize())

cus_order = []
max_length_list = 3
print(cus_order)
print(len(cus_order))
while len(cus_order) < max_length_list:
    item = input('Please select what you want from the menu ')
    cus_order.append(item)
    print(cus_order, '\n')
    print(len(cus_order))

print(f'Your final order is {cus_order}'.upper())

# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
#  print everything