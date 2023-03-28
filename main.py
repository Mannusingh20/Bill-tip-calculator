#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to our restaurant")
print("_________________________")
print("_________________________\n")

kul_log = input ("Enter the number of people: ")
kul_bill = input ("Enter the total bill: ₹")
tip_percent = input("Enter the the tip percent: ")

tip = float(tip_percent)/100 * float(kul_bill)

total = tip + float(kul_bill)
per_person = total / int(kul_log)

print(f"\nInitial bill = ₹{kul_bill}\nTip percent = {tip_percent}%\nTip = ₹{tip}\nTotal bill = ₹{total}\nPer person bill = ₹{round(per_person,2)}")
