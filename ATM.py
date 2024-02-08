pin=1222
attempt=2

while attempt >0:
    get=int(input("Enter your 4 Digit ATM pin :"))
     
    if get==pin:
        print("Pin verified succesfull")
        break
    else:
        attempt -=1
        print('Only one attempt left.Please enter your 4 Digit pin')
    if attempt ==0:
        print('Incorrect pin.Try again after 24 hours')