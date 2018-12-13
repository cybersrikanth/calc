def calc(a):
    try:
        print("Your answer: ",eval(a))
    except:
        print("error occured")

print("CALCULATOR".center(75, "-"))
while True:
    print("\ntype Q/q to exit\n")
    a=input("Enter an expression:")
    if (a.lower()=='q'):
        break
    calc(a)
