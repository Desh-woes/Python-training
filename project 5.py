country= input('what country are you from?')
if country.lower()=='canada':
    province= input('which province are you from?')
orderTotal= float(input('what is your order total'))
if country.lower()=='canada':
    if province.lower()=='alberta':
        orderTotal= orderTotal + orderTotal * 0.05
    elif province.lower()== 'ontario' or province.lower()=='new brunswick' or province.lower()=='nova scotia':
        orderTotal= orderTotal + orderTotal * 0.13
    else:
        orderTotal= orderTotal +orderTotal*0.06 + orderTotal*0.05
print('your total including taxes is $' + str(orderTotal))
