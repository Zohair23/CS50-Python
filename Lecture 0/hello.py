#just gong over the basics for now

name = input("What is your name? ")

#basic print
print("Hello, " + name)

#uses two "arguments", and also automatically adds a space between each argument
print("Hello,",name)

#print function automatically jumps to the next line (end = '\n'), to override this:

print("Hello, ", end="") #no jumping
print(name) #connects this print

#print function uses sep=" ", to automatically create a space between arguments, you can override by:

print("Hello,", name, sep = "???") #can be anything, here ??? used for fun

#note that singe quotes ('') and double quotes (""), work the same way, in python documentation
#it uses single quotes, but try to use double quotes only, try to be consistent with what you use

#WORKING WITH DOUBLE AND SINGLE QUOTES:
#you cant use double quotes inside double quotes it messes it up, e.g. print("hello, "friend""),
#instead use a mix of single and double quotes -> print('hello, "friend"')
print('hello, "friend"')

#if you really insist on using double quotes only
#you can use:
print("hello, \"friend\"")

#another way of writing that first example is:
print(f"Hello, {name}")
#this is called an f string, we added f and used curly brackets to input name, outputs are the same

#dealing with extra spaces
#input name(lets say we add way too many spaces at the start):
name2 = input("What is your name? ")

#removes whitespace from str
name2 = name2.strip()

#print (f string)
print(f"Hello, {name2}")

#capitalize user's name:
#input name:
name3 = input("What is your name? ")

#automatically capitalizes ONLY first letter
name3 = name3.capitalize()

#print
print("Hello,", name3)

#what if enter our full name, how do we capitalize that:
#input name:
name4 = input("What is your name? ")

#automatically capitalizes both names, here we are chaining functions, so both are applied, strip applied first
name4 = name4.strip().title()

#print
print("Hello,", name4)

#you can shorten it even further by:
#input name:
name5 = input("What is your name? ").strip().title()

#print
print(f"Hello, {name5}")

#split name into two and outputting the first name
name6 = input("What is your name? ").strip().title()

#split name into 2
first, last = name6.split(" ")

#print
print(f"Hello, {first}")
