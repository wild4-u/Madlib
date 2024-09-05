# MAdlib project
# code
# small fun project



# here we wil take all the input from the user and store in the variable !!
animal = input("enter a animal name : ")
place = input("enter a place name : ")
verb = input("enter a verb : ")
adjective = input("enter an adjective : ")
noun = input("enter a  noun : ")
adjective2 = input("enter again an adjective : ")
object = input("enter a  object : ")
animal2 = input("enter agian an  animal: ")
verb2 = input("enter a  verb : ")
object2 = input("enter again an object : ")

# here we will put the story in the varible with all users input in it and formating it !!
joke_story = f"""Why did the {animal }cross the road? To get to the {place } and {verb } the {adjective } 
                {noun }! But when it got there, it found a {adjective2 } {object } instead. 
                The {animal2 } laughed and said, "I guess I'll have to {verb2 } this {object2 } now!\n"""


print("so here is the joke : ")
print(joke_story)