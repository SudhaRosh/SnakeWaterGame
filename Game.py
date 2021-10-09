
import random

def gameWin (comp, you):
    if comp==you:
        return None
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
        elif comp=='w':
            if you=='g':
                return False
            elif you=='s':
                return True
        elif comp=='g':
            if you=='s':
                return False
            elif you=='w':
                return True

print("Comp Turn: Snake(s) Water (w) or Gun(g)? ")
randNo=random.randint(1,3)
print(randNo)
if randNo ==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='w'

you=input("Your Turn:snake(s) Water (w) or Gun(g) ?")
a= gameWin(comp,you)
print(f"Computer Chose {comp}")
print(f"You Chose {you}")

if a==None:
    print("The game is a Tie!")
elif a:
    print("You Win!")
else:
    print("you Lose!")
