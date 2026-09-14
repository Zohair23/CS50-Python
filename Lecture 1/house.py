name = input("What's your name? ")

#match
match name:
    case "Harry" | "Herminoe" | "Ron": #anyone with this name
        print("Gryffindor") #then print this
    case "Draco": #another case
        print("Syltherin")
    case _: #any other case
        print("Who?")

#use this if you dont want to keep using if, e.g. if name = "Harry" ...