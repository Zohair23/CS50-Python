#while loop
i = 3

#loop until i turn to 0
while i != 0:
    print("Meow")
    i = i - 1

#another version (going up)
i = 0

while i < 3:
    print("Meow2")
    i += 1 # i = i + 1  




#for loop
for i in [0, 1, 2]: #here a list is used
    print("Meow")

#another for loop
for i in range(3): #here a range function is used, starts from 0, 1, .. and stops at 2 (3 values)
    print("Meow2")

#another very similar version
for _ in range(3): # use _ here instead of i, since we dont ever use i, _ is just better (not required)
    print("Meow3")



#another way (no loops)
print("Meow\n" * 3, end="") # \n to change to new line every time you repeat and end = "" to stop an
                            # an extra blank line from being printed




#looping if statements
while True:
    n = int(input("What's n? "))
    if n < 0: #is n a negative numnber?, loop again if it is
        continue #keep looping
    else:
        break #stop otherwise

#shorter version
while True:
    n = int(input("What's n? "))
    if n >= 0: # is n is positive number or zero, stop
        break

#here we used n, but if its zero it wont wont, so change that later when necessary
for _ in range(n):  
    print("Meow")


#using functions
def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("What's n bro? "))
        if n > 0:
            return n

main()