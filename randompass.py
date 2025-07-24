import random
import string
import sys
from random import choice

import pyperclip

my_password = []
print("---- Random Password Generator ------")
pswd_length = int(input("Enter Password Length : "))

if pswd_length < 8 or pswd_length > 20:
    print("Password Minimum Length Is 8 and Maximum Length Is 20")
    sys.exit()

else:
    Passeword_List = string.ascii_letters + string.punctuation
    for a in range(pswd_length):
        my_password.append(random.choice(Passeword_List))

    string_pswd = "".join(my_password)
    print(f"Gernerated Password : {string_pswd}")

    choice = input(f"Do You Want To Copy {string_pswd} ?")
    if choice.lower() == "yes":
        pyperclip.copy(string_pswd)
        print("Password Has Been Copied")