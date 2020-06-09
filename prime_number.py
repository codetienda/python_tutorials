
num=input("Enter a number to check : ")# request a number from user 
num=int(num)# change entered number to integer

if num>1:# we continue for positive number
	for x in range(2,num):
		if num%x==0:
			print(num," is not prime number")
			print(x," times",num// x," is ",num)
			break #here we break for loop
	else:
		print(num," is prime number")
else:
	print("The entered number is not prime number")
