# Restaurantname = "Khan Restaurant"
# Address = "Baldia Town"
# Speciality = "Beef Biryani"
# Ph_number = "03082505730"
# City = "Karachi"
# Is_Fivestar = True
#
# print(f"Restaurant Name Is {Restaurantname}.\nLocated In {Address}.\nSpeciality Is {Speciality}.\nPhone Number Is {Ph_number}.\nCity {City}.\nFive Star{Is_Fivestar}")

# Restaurantname = input("Enter Restaurant Name")
# Address = input("Enter Address")
# Speciality = input("Enter Speciality")
# Ph_number = input("Enter Ph_number")
# City = input("Enter City")
# Is_Fivestar = input("Enter Rating")

print("Dholo Bholo Halwa Puri Shop")
Puris = int(input("How Many Puri You Want"))
Cholay = int(input("How Many Cholay plate You Want"))
Allu = int(input("How Many Allu You Want"))
Halwa = int(input("How Many Halwa You Want"))

perpuri = 50
percholay = 100
perallu = 80
perhalwa = 150

totalpuri = perpuri * Puris
totalcholay = percholay * Cholay
totalallu = perallu * Allu
totalhalwa = perhalwa * Halwa

totalbill = totalpuri + totalcholay + totalallu + totalhalwa
tax = totalbill * 0.16
total = tax + totalbill
discount = total * 0.5
bill_after_dis = discount - total
print(f"Total Bill Is : ",totalbill,"\ntax is : ",tax,"\nTotal Is :",total,"\nDiscount Is : ",discount,"\nAfterDiscount Total Is : ",bill_after_dis)
