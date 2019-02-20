print("Hi there!")
name = input("What's your name?: ")
print("Cool name, " + name + ".")
print("As you perhaps already know " + name + ", this program will help you check your own mood. So lets start.")
mood = input("How do you feel today?: ")
if mood == "happy":
    print(" It is great to see you happy")
elif mood == "nervous":
    print(" Take a deep breath 3 times.")
elif mood == "sad":
    print(" Cheer up, life is too short to be sad.")
elif mood == "exited":
    print(" Great! Me too.")
elif mood == "relaxed":
    print(" Very good. relaxing heals you body and mind.")
else:
    print(" Sorry! This kind of mood is unknown to me. ")
