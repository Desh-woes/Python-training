##import csv
##fileName= 'demo.txt'
##readFile= open(fileName, 'r')
##allfileContent= readFile.read()
##print(allfileContent)

##readFile= open(fileName, 'r')
##firstLine= readFile.readline()
##print(firstLine)
##secondLine= readFile.readline()
##print(secondLine)

##accessMode= 'r'
##with open(fileName, accessMode) as myCSVfile:
##    datafromFile= CSV.reader(myCSVfile)
    
##fileName= 'demo.txt'
##accessMode= 'r'
##with open(fileName, accessMode) as myCSVfile:
##    datafromFile= CSV.reader(myCSVfile)

##animalFile= open('Nigeria.txt', 'r')
##allfileContents= animalFile.read()
##print(allfileContents)

# CSV function 
##fileName='Nigeria.txt'
##accessMode= 'r'
##with open(fileName, accessMode) as myCSVfile:
##    datafromFile= csv.reader(myCSVfile)
##    for secondRow in datafromFile:
##        print(':'.join(secondRow))

# Grade calculator
##grade= int(input('please enter your score'))
##if grade >= 90:
##    print('you got a grade of A')
##elif 80<= grade <= 89:
##    print('you got a grade of B')
##elif 70<= grade <= 79:
##    print('you got a grade of C')
##elif 65<= grade <= 69:
##    print('you got a grade of D')
##elif 56<= grade <= 64:
##    print('you got a grade of E')
##elif grade <= 55:
##    print('you got a grade of F, you\'re a failure')
##print('thanks for checking your result')

# While loop
##b=1
##while b <= 10:
##    print (b)
##    b +=1

# For loop on integers
##fs= ['bread', 'milk', 'meat', 'beef']
##print(fs)
##for food in (fs):
##    print('i want ' + food)

#introduction to numpy.
##import numpy as np
##mylist = [1,2,3,4]
##myarray = np.array(mylist)
##print(myarray)


#python for D&D
##List=[]
##for numbers in range(1,200):
##    if (numbers % 4 != 0) and (numbers % 3 == 0 or numbers % 5 ==0):
##        List.append(numbers)
##for steps in List:
##    print(steps)

##mySquares= {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100, 11:121, 12:144, 13:169, 14:196, 15:225}
##print(mySquares[5])
##Days=['Monday', 'Teusday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
##print(Days[5])

##import random
##print(' welcome to this beatiful game where you get to try your luck\neach dice has sixty four sides. Try to get a 64 to win a prize :) goodluck!!')
##while 1>0:
##    value=input('please enter \'y\' to take a spin')
##    if value=='y':
##        for steps in range(1):
##            print(random.randint(1,65))

    

