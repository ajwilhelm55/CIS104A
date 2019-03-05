size = 10
i = 0
userValue = []

print("List of Integers: ")

while i < size:
    userValue.append(int(input("Enter an integer: ")))
    i = i + 1

print("Now the reverse")
i = 9
while i >= 0:
    print(userValue[i])
    i = i - 1 
    
