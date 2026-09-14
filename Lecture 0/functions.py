#define a function using keyword def
#you can input parameters into function
#here to is the name of the person, then it is used to print hello and the person's name using
#an f string
def hello(to):
    print(f"Hello, {to}")

#input
name = input("Whats your name? ")

#we called the function here, unless we call it, it wont work
hello(name)

#in functions you can set parameters values to default values, so even if the user
#doesnt enter the parameter value, the default value is used in the function
#for e.g.


def hello2(to="world"):
    print("Hello,", to)

#calling just this gives me output Hello, world
hello2()

#but if i input
name2 = input("Whats your name? ")

#output here would be Hello, -persons's name- , the parameter to is overwritten by the name2
hello(name2)

#note: in python, functions should be defined above from where it is called, if you call a function
#and the function is defined below, it won't work, functions must be at the top(must already exist)

#using def main() can help here

#main function
def main():
    name = input("Whats your name? ")
    hello(name)

#hello function
def hello(to="world"):
    print("hello,", to)

#have to still call here, under the hello function
main()

#this will work

#use return to return a value

## n ** 2, means n to the power of 2, or just use pow(n,2)