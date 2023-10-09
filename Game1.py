import random

print("Lets play a game")
print("computer's turn: Stone(s), Paper(p), Scissor(c) ")
random_no = random.randint(1,3)
#print(random_no)

if random_no == 1:
    comp = 's'
elif random_no == 2:
    comp = 'p'
else:
    comp = 'c'


print(comp)

user = input("User's Turn: Stone(s), Paper(p), Scissor(c)")


if comp == 's':
    if user == 's':
        print("Its a tie")
    elif user == 'p':
        print("user won")
    elif user == 'c':
        print("computer won")
    else:
        print("Invalid input")

elif comp == 'p':
    if user == 's':
        print("computer won")
    elif user == 'p':
        print("its a tie")
    elif user == 'c':
        print("user won")
    else:
        print("Invalid input")

elif comp == 'c':
    if user == 's':
        print("user won")
    elif user == 'p':
        print("computer won")
    elif user == 'c':
        print("its a tie")
    else:
        print("Invalid Input")

else:
    print("invalid input")
