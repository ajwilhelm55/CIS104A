print("I will tell you which American Patriot is on your money!\nI'm also a history buff!, so I will give you a fun fact to impress your friends with!")
dollarNumber = int(input("What denomination is your banknote? "))

if dollarNumber == 1:
    print("George Washington is on your one dollar bill!\nFun Fact: George Washington didn't like political parties, he thought they would bring an end to American Politics.")
elif dollarNumber == 2:
    print("Thomas Jefferson is on your two dollar bill!\nFun Fact: Thomas Jefferson was one of the only American Presidents that wasn't a Christian.")
elif dollarNumber == 5:
    print("Abraham Lincoln is on your five dollar bill!\nFun Fact: Abraham Lincoln was the tallest president at 6 feet 4 inches.")
elif dollarNumber == 10:
    print("Alexander Hamilton is on your ten dollar bill!\nFun Fact: Alexander Hamilton was Americas first Treasury Secretary, in order to protect tax payments from being stolen he established the Coast Guard.")
elif dollarNumber == 20:
    print("Andrew Jackson is on your twenty dollar bill!\nFun Fact: Andrew Jackson fought the indians, then adopted two as his children.")
elif dollarNumber == 50:
    print("Ulysses S. Grant is on your fifty dollar bill!\nFun Fact: Ulysses S. Grant was kicked out of the military for being a drunkard before he was President.")
elif dollarNumber == 100:
    print("Benjamin Franklin is on your one hundred dollar bill!\nFun Fact: Benjamin Franklin only had two years of formal education.")

else:
    print("No banknote exists. You don't have United States Currency!!!")