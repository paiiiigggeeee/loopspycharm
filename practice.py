# computers can repeat the same task over and over without getting tired

# For loops are counting loops. If you know how many times you need to repeat a task

# While loops are if you aren't sure how many times you need to repeat a task

# While loops can check to see if the input is valid and ask to try again,etc


number_of_credits = int(input('How many credits are you taking this semester?'))

while number_of_credits < 0:
    print('Error')

if