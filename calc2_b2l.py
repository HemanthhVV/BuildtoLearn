from greet_build_to_learn import *
print("im calc bot and i can do simple operation")
Q_msg=['q','quit','bye','enough','good bye','see','e','exit']
a=input().split()
while a[0] not in Q_msg:
    num1=float(a[1])
    num2=float(a[2])
    if a[0]=='add':
        print(num1+num2)
    elif a[0]=='sub':
        print(num1-num2)
    elif a[0]=='mul':
        print(num1*num2)
    elif a[0]=='div':
        print(num1/num2)
    a=input().split() 
        
    
    
    
