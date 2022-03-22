#Tells you what generation you're in based on your age
age = int(input("What is your age?"))
if age < 24:
    print("You are part of Generation Z!")
elif age > 24 and age < 41:
    print("You are part of Millenials!")
elif age > 40 and age < 57:
    print("You are part of Generation X!")
elif age > 56 and age < 76:
    print("You are part of Baby Boomers!")
elif age > 75:
    print("You are part of The Silent Generation!")
