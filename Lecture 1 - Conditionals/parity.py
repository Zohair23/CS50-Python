#we know this
# + (addition)
# - (subtraction)
# * (multiplication)
# / (division)
# % (modulo)


#here iseven() takes in an input and is used in the condition, the output is a boolean
#so if it is True, then it prints even, prints odd otherwise
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#reduced iseven() function
# def is_even(n):
#    return True if n % 2 == 0 else False 

#reduced iseven() function even further
# def is_even(n):
#    return n % 2 == 0 #inside the bracket, the output is either True or False

main()