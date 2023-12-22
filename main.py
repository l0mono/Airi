import random

usr = input("Enter your name > ")
if usr:
    pass
else:
    usr = "You"

li = ["そうなんだ","確かに","いいね","ううん","なるほど","へ〜"]

while True:
    message = input("Enter message > ")
    if message == "さようなら":
        break
    print(("{0}: {1}").format(usr,message))
    res = random.choice(li)
    print(("Airi: {}").format(res))