print("Hello, World!")

name = input("What is your name? ")

if name:
    print("Hello,", name)
else:
    print("No name provided.")

for i in range(5):
    print(i)

numbers = [1, 2, 3, 4, 5]
print(len(numbers))

def square(x):
    return x * x

print(square(10))

value = None
flag = True

if flag and value is None:
    print("Done")