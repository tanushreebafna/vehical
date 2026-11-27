print("Parking System")

vehicle_no = input("Enter Vehicle Number: ")
type = input("Enter Vehicle Type (Two/Four/Heavy): ")
hours = int(input("Enter Hours: "))

if type == "Two":
    fee = hours * 20
elif type == "Four":
    fee = hours * 50
elif type == "Heavy":
    fee = hours * 100
else:
    print("Invalid Vehicle Type")
    exit()

print("Vehicle Number:", vehicle_no)
print("Vehicle Type:", type)
print("Hours:", hours)
print("Parking Fee: Rs.", fee)