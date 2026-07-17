#if statement:
#mobile battery:
'''ch=int(input('enter the battery percentage:'))
if ch<=20:
    print('ALERT: Battery Low')'''

#discount:
'''discount=int(input('enter discount:'))
price=int(input('enter price:'))
if discount:
    price-=price*(discount/100)
print('price:',price)'''

#if-else:
#login:
'''data={'sreeja@gmail.com':'sree123',
      'vanga@gmail.com':'vanga123'}
email=input('enter email:')
password=input('enter password:')
if data.get(email)==password:
    print('Login Successful!')
else:
    print('Login Invalid')'''

#otp verification:
'''import random #random is library to get a random value.
otp=random.randint(1111,9999)
print('Your OTP is:',otp)
enter_otp=int(input('enter OTP:'))
if otp==enter_otp:
    print('Verified Successfully!')
else:
    print('Invalid OTP')'''

#elif and nested if:
#order time and order failed:
'''hr,min=list(map(int,input('enter the time (HH:MM):').split(':')))
fare=0
price=350
if hr in range(0,23) and min in  range(0,59):
    if hr in range(8,16):
        fare=40
    elif hr in range(16,23):
        fare=100
    elif hr in range(0,8):
        fare=150
    print('Total Fare is',fare)
else:
    print('Invalid Time')'''





    




