#how to check number is prime or not.

#prime number is always greater than 1

# number divided by 1 and itself

# 19 = 1 and 19 only:prime number
#28 =1,2,4,7,14,28 :not prime number



num =int(input("please enter the number: "))

count =0

if num>1 :
    for i in range(1, num+1):
        if(num%i)==0:
            count =count+1
    if count==2:
        print("number is prime")
    else:
        print("number is not prime")
