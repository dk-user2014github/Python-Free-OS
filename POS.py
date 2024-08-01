import os

print("Starting OS")
a = input(">>>")

def unknown_command():
    global a
    print("Unknown command: " + a)
    a = input(">>>")

def help():
    global a
    print("help, info, calc, text, game,")
    a = input(">>>")

def info():
    global a
    print("Python OS, version 1.1, by Lfolix")
    a = input(">>>")

def calc():
    global a
    c1 = int(input("1-"))
    c2 = int(input("2-"))
    c3 = input("Enter command-")

    if c3 == "+":
        print(c1 + c2)
        a = input(">>>")

    if c3 == "-":
        print(c1 - c2)
        a = input(">>>")

    if c3 == "*":
        print(c1 * c2)
        a = input(">>>")

    if c3 == "/":
        print(c1 // c2)
        a = input(">>>")

def text():
    global a
    txt = input("Text >>>")
    a = input(">>>")

def game():
    global a
    game = 12 or 65 or 43
    game2 = int(input("Type number >>>"))

    if game2 > game:
        print("This is larger!")
        a = input(">>>")

    if game2 < game:
        print("This is less!")
        a = input(">>>")

    if game2 == game:
        print("This is right!")
        a = input(">>>")

while True:
    if a == "help":
        help()

    elif a == "info":
        info()

    elif a == "calc":
        calc()

    elif a == "text":
        text()

    elif a == "game":
        game()

    else:
        unknown_command()

    
