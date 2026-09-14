x = int(input("What's x? "))
y = int(input("What's y? "))

#condition, if this , then: .....
if x < y:
    print("x is less than y")

#another condition
if x > y:
    print("x is greater than y")

#another condition
if x == y:
    print("x is equal to y")


#use elif, to not keep repeating if statements
#use else at the end, if not condition is met, do: ...
a = int(input("What's a? "))
b = int(input("What's b? "))

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")




#another example using or
x = int(input("What's x? "))
y = int(input("What's y? "))

#you could also use if x != y here for the initial if
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")


#using and in if's
score = int(input("Score: "))

#you could also shorten down to 90 <= score <= 100 and so on ...
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#you could also take an assumption that the score peaks at 100
#and change it to if score >= 90: and so on .... score >= 80: .....



