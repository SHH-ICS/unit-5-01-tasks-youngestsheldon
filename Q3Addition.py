import random

robert = int(random.randint(1, 100))
jamis = int(random.randint(1, 100))

noam = robert + jamis

blapis = input(robert, "+", jamis, "= ?")

if noam == blapis:
    print("corect")
else:
    print("wrong")