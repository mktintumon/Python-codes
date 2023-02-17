def first_fn() :
    print("hello")
    print("world")

first_fn()

# parameters
def sec_fn(name):
    print("My name is " , name)

sec_fn("Sobhik")


# default  arguments
def third_fn(crs="MCA"):
    print("My Course is " , crs)

third_fn("MSC")
third_fn()


# passing list
myList = ["A", "B", "C", "D", "E", "F"]

def printer(items):
    for x in items:
        print(x , end="  ")

printer(myList)


# recursion
print("\n")
def recursion(n):
    if(n==1):
        return 1
    else:
        return n * recursion(n-1)

print("Factorial -->  " ,recursion(5))
