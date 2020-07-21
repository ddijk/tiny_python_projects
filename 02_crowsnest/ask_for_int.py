x = int(input("Geef een waarde"))


def processInput(val):
    if val < 0:
        val = 0
        print("Negative changed to zero")
    elif val == 0:
        print("Zero")
    elif val == 1:
        print("Single")
    elif val > 1:
        print("Multiple")


processInput(x)
