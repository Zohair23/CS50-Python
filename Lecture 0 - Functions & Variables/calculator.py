#int function used here to make input an integer, if you dont use it, it will be a string
x = int(input("Whats x? "))
y = int(input("Whats y? "))

print(x+y)

#float function this time(decimal points)
a = float(input("What is a? "))
b = float(input("What is b? "))

print(a+b)



#rounding numbers, round function: round(number[, ndigits]), you can change the parameter, so that
#you can choose how much it rounds to or what nearest int

#basic round
x2 = float(input("Whats x? "))
y2 = float(input("Whats y? "))

z2 = round(x2+y2)

print(z2)


#altered round function
#rounding numbers, round function: round(number[, ndigits]), you can change the parameter, so that
#you can choose how much it rounds to or what nearest int
x3 = float(input("Whats x? "))
y3 = float(input("Whats y? "))

#since we add (,2), so round to 2 number of digits e.g. 0.67
z3 = round(x3/y3,2)

print(z3)




#formatting number
x4 = float(input("Whats x? "))
y4 = float(input("Whats y? "))

z4 = round(x4+y4)

# same number, but automatically adds , inbetween, e.g. 10000 becomes 10,000, f string used here
# (:,) is adding this comma
print(f"{z4:,}")



# f string way of rounding to 2 number of digits
x5 = float(input("Whats x? "))
y5 = float(input("Whats y? "))

z5 = x5/y5

#here is where it rounds to 2 number of digits, e.g. 0.67
print(f"{z5:.2f}")