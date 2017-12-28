friendList= ['Rotimi, 17','\nNnadozie, 20','\nnelly, 18','\nFunmibi, 17','\n pelumi, 17']
area= len(friendList)
fileName= 'fileone.csv'
WRITE= 'w'
Append= 'a'
file=open(fileName, mode=WRITE)
##file.write('i am getting tired\n')
##file.write('alu shaaaa')
for steps in range(area):
    file.write(friendList[steps])
file.close
print('program written succesfully')
