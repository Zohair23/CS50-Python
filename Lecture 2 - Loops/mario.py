def main():
    height = int(input("Enter number of bricks going up: "))
    print_column(height)

#making mario bricks (stacked up)
def print_column(n):
    for _ in range(n):
        print("#")

    #or you could use
    #print("#\n" * n, end="")

main()



#making mario bricks (across)
def main2():
    length = int(input("Enter number of bricks going across: "))
    print_row(length)

def print_row(m):
    print("?" * m)
 

main2()



def main3():
    square_size = int(input("Enter square size: "))
    print_square(square_size)

def print_square(o):
    for i in range(o): #outer loop
        for j in range(o): #inner loop
            print("#", end="") #print the bricks in that row
        print() #outer loop print (go to a new line)

    #shorter version
    #for i in range(o):
    #    print("#" * o)

main3()