import random
import string
import sys
import pyperclip

# Empty List
uper_list ,lower_list,Special_list,Number_list=[],[],[],[]

Bari_abcd = string.ascii_uppercase
Choti_abcd = string.ascii_lowercase
Number = string.digits
Special = string.punctuation

print("---- Random Password Method 2 -----" )
uper_length=int(input("How many upper letter you went?"))
if uper_length < 1 or  uper_length > 8:
    print("Invalid length ")
    sys.exit()
lower_length=int(input("How many lower letter you went?"))
if lower_length < 1 or  lower_length > 8:
    print("Invalid length ")
    sys.exit()
number_length=int(input("How many number  you went?"))
if number_length < 1 or  number_length > 8:
    print("Invalid length ")
    sys.exit()
special_length=int(input("How many special letter you went?"))
if special_length < 1 or  special_length > 8:
    print("Invalid length ")
    sys.exit()

for a in range(uper_length):
    uper_list.append(random.choice(Bari_abcd))

for a in range(lower_length):
    lower_list.append(random.choice(Choti_abcd))

for a in range(number_length):
    Number_list.append(random.choice(Number))

for a in range(special_length):
    Special_list.append(random.choice(Special))

# print(uper_list)
# print(lower_list)
# print(Number_list)
# print(Special_list)

password = uper_list + lower_list + Number_list + Special_list
random.shuffle(password)
random.shuffle(password)
string_password = "".join(password)
print(f"String password is : {string_password}")