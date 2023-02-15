print("I am a VITIAN")

GPA = 9
GPA = 10

if(GPA > 9) :
    print("Attended more classes")
else :
    print("Attended less classes")


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

a , b , c = "govind" , "sobhik" , "kishan"
print(a ," " , b ," " , c)


#list
x1 = ["hum", "tum", "wo"]
print(x1)

#tuple		
x2 = ("hum", "tum", "wo")	
print(x2)

#range	
x3 = range(10)	
print(x3)

#dict
x4 = {"name" : "Mohit", "age" : 24}	
print(x4)

#set
x5 = {"apple", "banana", "cherry"}	
print(x5)


#string
s = "Me"
s1 = """I am Mohit kumar 
Doing MCA from VIT vellore"""
print("Superb " , s)
print("Intro -> " ,s1)


# format string
name = "Mohit"
age = "24"
course = "MCA"
detail = "My name is {} and my age is {} and my course is {}"
#print(detail.format(x1[0],x1[1],x1[2]))
print(detail.format(name,age,course))



