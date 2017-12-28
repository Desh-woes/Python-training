guestList= []
name= ''
while name != 'y':
    name = input('enter guest name (enter done if no more names :)')
    guestList.append(name)
guestList.remove('y')
guestList.sort()
for guestList in guestList:
    print(guestList)
    
    
