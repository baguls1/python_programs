# factorial number n=5 1*2*3*4*5=120


factorial =1
num=5

if num<0:
    print("factorial does not exsit for negative number")

elif num==0:
    print("factorial of number 0 is always 1")

else:
    for i in range(1, num+1):
        factorial =factorial *i
    print(" the factorial of ", num, "is", factorial)