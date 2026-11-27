
print("Vehicle Parking")

type = input("Enter vehicle type (two/four/heavy): ")
hours = int(input("Enter hours: "))

if type == "two":
    fee = hours * 20
elif type == "four":
    fee = hours * 50
elif type == "heavy":
    fee = hours * 100
else:
    print("Invalid vehicle type")
    exit()

print("Vehicle type:", type)
print("Hours:", hours)
print("Parking fee: Rs.", fee)
