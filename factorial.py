'''
This program is to find factorial of a number
Program flow:-
1)input a number from user
2)set a variable to zero
3)do a while loop and multiply the variable with the input and repeatedly decrease the input one by one
'''
num=int(input("Enter your number: "))
copy_num=num
var=1
while num>0:
    var=var*num
    num-=1
print("Factorial of",copy_num,"is",var)