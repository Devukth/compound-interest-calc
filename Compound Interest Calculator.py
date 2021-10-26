def find_compound_interest(p, t, r):
    amount = p * (pow((1 + r / 100), t))
    return amount - p

p = float(input("How much money did you put in the bank? "))
t = float(input("How much time has it been since you put the money in the bank? (in years) "))
r = float(input("What is your rate of interest "))
print("Your interest is $" + str(find_compound_interest(p, t, r)))
print("Your amount is $" + str((find_compound_interest(p, t, r) + p)))
 