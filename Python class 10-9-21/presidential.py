#tells you if you are eligible to run for president
age = int(input("Age:"))
borninus = str(input("Born in the US? (Yes/No)"))
yearsofresidency = int(input("Years of residency:"))
if age < 35:
    print("You are not eligible to run for president.")
elif borninus == "No":
    print("You are not eligible to run for president.")
elif yearsofresidency < 14:
    print("You are not eligible to run for president.")
else:
    print("You are eligible to run for president!")
