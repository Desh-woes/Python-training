import random
print(' welcome to this beatiful game where you get to try your luck\neach dice has sixty four sides. Try to get a 64 to win a prize :) goodluck!!')
while 1>0:
    value=input('please enter \'y\' to take a spin')
    if value.upper()==('Y'):
        for steps in range(1):
            print(random.randint(1,6))
    elif value.upper()=='Q':
        exit()
