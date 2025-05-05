iv = float(input("Initial Investment "))
length = float(input("How long (days) "))
interest = float(input("Daily Gain (Ex. 1% = 1.01) "))
i = 1
while i < length+1:
    print("%.2f" % iv)
    iv = (iv*interest)
    i += 1

input("")