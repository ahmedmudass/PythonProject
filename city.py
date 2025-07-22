import random as rd
import sys

# city = ["karachi","Islamabad","Swat","Rawalpindi","Sukkur","Lahore","Quetta","Multan","Faislabad","Peshawar"]
#
# print(city)
# print(rd.sample(city,3))
# rd.shuffle(city)
# print(city)
# print(rd.choice(city))

print("********** Random Number Guessing Game ********\n")
computer_num = rd.randint(1,20)
Lives = 3

while Lives > 0:
    user_input = int(input("Enter Any Number Between 1 to 20 : "))

    if user_input == computer_num:
        print("Congratulations You've Guessed!!")
        sys.exit()

    else:
        Lives -= 1

        if user_input > computer_num:
            print("* Hint : Think Lower Number")
        elif user_input < computer_num:
            print("* Hint : Think Higher Number")

        if Lives == 0:
            print("Lives End")
        else:
            print(f"{Lives} Remaining")