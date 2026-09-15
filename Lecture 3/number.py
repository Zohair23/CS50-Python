#here if we dont enter an integer, python runs into a ValueError
x = int(input("What's x? "))

print(f"x is {x}")

#Attempt 1
#to fix this we use exceptions
try: #try this
    y = int(input("What's y? "))
    print(f"y is {y}")
except ValueError: #catching that ValueError
    print("y is not an integer") #print this message if we run into this ValueError


#Attempt 2
#we need to try and keep minimal code to check, so lets take out the print in the end
try:
    z = int(input("What's z? "))
except ValueError:
    print("z is not an integer")

# we will run into a NameError here, even though we did a good thing
# NameError because if z doesn't work in try, then we won't be able to print (so then z won't be defined)
print(f"z is {z}")



#Attempt 3
#to fix this, python allows else in exceptions
try:
    a = int(input("What's a? "))
except ValueError:
    print("a is not an integer")
else: #add an else
    print(f"a is {a}")



#Attempt 4
#incorporating While loop, to allow the user to keep entering until they get it right
while True:
    try:
        b = int(input("What's b? "))
    except ValueError:
        print("b is not an integer")
    else: #add an else
        break #we dont need to print here, because it would keep repeating until we get the right value
              #then we break

#you can print here now
print(f"b is {b}")



#Improvement, to save it as a function
def main():
    user_input = get_int()
    print(f"c is {user_input}")

def get_int():
    while True:
        try:
            c = int(input("What's c? "))
        except ValueError:
            print("c is not an integer")
        else: #add an else
            break #we dont need to print here, because it would keep repeating until we get the right value
                  #then we break
    
    return c

main()