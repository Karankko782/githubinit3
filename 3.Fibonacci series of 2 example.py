#printing all the series
n=int(input("enter a no:"))
a=1
b=1
temp=0
for i in range(0,n):
    if(i==0):
        print(0,end=" ")
    elif(i==1 or i==2):
         print(1,end=" ")
    elif(i>2):
        print(a+b,end=" ")
        temp=b
        b=a+b
        a=temp

#printing last number of the series
def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

print("\n",Fibonacci(6))