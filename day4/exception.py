b=int(input("enter a number"))

try:
    a=20/b
    print(a)
    print("no problem")
except ZeroDivisionError:
    print("cant divide")



