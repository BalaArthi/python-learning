
currency = input("Choose your currency (USD/JPY/GBP/EURO/RUB): ").upper()

if currency == "USD":
    amount = float(input("Enter amount:"))
    to_inr = amount * 86.63
elif currency == "JPY":
    amount= float(input("Enter amount:"))
    to_inr = amount * 0.58
elif currency == "GBP":
    amount = float(input("Enter amount:"))
    to_inr = amount * 112.64
elif currency == "EURO":
    amount = float(input("Enter amount:"))
    to_inr= amount * 94.82
elif currency == "RUB":
    amount = float(input("Enter amount:"))
    to_inr = amount * 1.06
else:
    print("Invalid currency")
print(f"{amount} {currency} is {round(to_inr,2)} INR ")
