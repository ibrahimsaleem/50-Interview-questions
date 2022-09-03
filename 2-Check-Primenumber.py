
# Program to check if a number is prime or not

#num = 23
#or taking input from user
num = int(input("Enter Number to check if its prime or not : "))
count = 0

# prime numbers are greater than 1
if(num>1):
    # checking for if the  number is divisiable by any number below it
    for i in range(2,num):
        if(num%i==0): 
             # if the number idivisiable by any number below it, set count = 1
            count=1
            # break out of loop
            break

    if count==1:
        print(num,"is not a Prime Number")
    if count==0:
        print(num,"is Prime Number")

else: print("1 is not a prime number or a composite number!!")
