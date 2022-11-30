n = int((input("Enter :")))
fact = 1  
for i in range(1,n+1):
    fact = fact * i      
print ("The factorial of  is : ",end="")
print (fact)
sum = 0
for i in str(fact):
    sum = sum + int(i)
print(sum)