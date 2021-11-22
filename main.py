"""
Write a program that asks a user for two integers.  Print "YES" if exactly one of them is odd and print "NO" otherwise
"""
print("Give me two integers, and I will determine wether one of them is odd or not ")
firstInteger = int(input("Enter the first integer. "))
secondInteger = int(input("Enter the second Integer. "))
#asks the user for two integers to determine which is odd
if firstInteger % 2 == 1 and secondInteger % 2 ==0 or firstInteger % 2 == 0 and secondInteger % 2 ==1:
  print ("One of the values is odd")
else:
  print ("There is not only one odd value")
#determines wether one of the values is odd
