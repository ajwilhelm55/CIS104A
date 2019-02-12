import math
print("Your about to be rewarded with your own personal lucky number!")
userAge = int(input("How old are you?"))
userDay = int(input("What day of the month were you born?"))
x = userDay * userAge
luckyNumber = math.sqrt (x)
luckyNumber = math.ceil (luckyNumber)
print("Your personal lucky number is!")
print(luckyNumber)      
              
              
      
      