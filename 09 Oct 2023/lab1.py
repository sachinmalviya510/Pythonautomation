#String
#string functions
#String Immutable in nature- they can't changed once created
name= "sachin"
print(name)
#Capitalize
result = name.capitalize()
print (result)
print (name)

#UpperCase
result2 = name.upper()
print(result2)

#lowercase
result2 = name.lower()
print (result2)

#Swapcase
name1 = "PraMod"
print(name1)

#title
result4= "sachin malviya"
print(result4.title())

t1 = 'duttaji'
t2= "pramod ji"
print(t1.capitalize())
print(t2.upper())

#t1 is ref  or variable name, "duttaji" which is stored in memory

#length always starts from 1
name = "dutta"
print(len(name))

#replace
text ="hello world"

#replace
text = "hello world"
#result_rep=text.replace("world"+"sachin")

# find()
#returns the lowest index of a substring in the string
#retruns -1 if the substring is npt found

text ="hello world"
index = text.find("world")
print(index)

#count - count the character
#Space also a character
count = text.count("l")
print(count)

