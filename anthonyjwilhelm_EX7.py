def multiplication(i):
    c = 1
    total = i[0]
    while c < len(i):
        total = total * i[c]
        c = 1 + c
    return(total) 



def createarray():
    userValue1 = []
    i = 1
    while i != 0:
        i = int(input("Start Typing:"))
        if i != 0:
            userValue1.append(i)    
    return(userValue1)



print("This program multiplies all the numbers entered:")      
print(multiplication(createarray() ))

    
    