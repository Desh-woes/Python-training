import random
print('each dice has six sides. Try your luck to earn six points!!!!')
while 1>0:
    value= input('please enter "y" to take a spin')
    for x in range (1):
        output=print(random.randint(1,7))
        if output==6:
            print('you\'ve hit jackpot!!!')
