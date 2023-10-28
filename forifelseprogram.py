n=input()
for letter in n:
    print(n)
    x=len(letter)
    if (x%2==0):
        print("Even word")
    elif(x%2!=0):
        print("odd word")