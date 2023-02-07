
age = input("Please enter your age: ")

if int(age) > 18:
    name = input("input your name: ")
    print(f"Welcome {name}")
else:
    print("shoma kodak hastid...")
print(type(age).__name__)
print(type(int(age)).__name__)
