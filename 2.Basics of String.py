#Example1
str1="no one"
str2="arya stark"
for letter in str1:
    print(letter)

print("\n")

x=str2.split()
y=set(x)
print(len(str2))
for word in y:
    print(word)

print("\n")

#example2
str="arya stark"
z=set(str)
print(z)
s=[]
for word in z:
    print(word)
    s.append(word)
print(list(s))


print("\n")

#example3
user_input = input("Enter your sentence here: ")
sentence = user_input.split()
text = set(sentence)
dict_sentence = {}
s=0
for i in text:
    x = user_input.count(i)
    s=s+x
    dict_sentence.update({i:s})
print(dict_sentence)


print("\n")

#changes of example 3
user_input = input("Enter your sentence here: ")
sentence = user_input.split()
text = set(sentence)
dict_sentence = {}
x =len(text)
for i in text:
    for j in range(1,x+1):
        dict_sentence.update({i:j})
        print(dict_sentence)
