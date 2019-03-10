
i = 1

userValue1 = []
userValue2 = []

print("Double The Keyboard Numbers")

while i != 0:
    i = int(input("Start Typing"))
    if i != 0:
        userValue1.append(i)
        
i = 0
while i < len(userValue1):
    userValue2.append(userValue1[i] * 2)
    i = i + 1
    
    
print(userValue2)


