def add_or_divide(x,y,choice):
    if choice == "addition":
        return int(x) + int(y)
    else:
        return int(x) / int(y)

x = input("Enter value for x:")
y = input("Enter value for y:")
choice = input("type addition to add these two numbers or type anything else to divide these two numbers")
print(add_or_divide(x,y,choice))