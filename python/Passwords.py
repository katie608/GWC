from hashlib import *

inventory={"Katie":"dolphin11", "Ashley":"tacosandsushi"}

username=input("What is your usernamename?")

password=input("What is your password?")

#print(sha256(password.encode('utf-8')).hexdigest() )



if password==username:
    print("Your password is correct")
elif not username in inventory.keys():
    print("You have not signed up yet.")
    new_value_dictionary[(input("What do you want your username to be?")):(input("What do you want your password to be?"))]
else:
    print("Your password is incorrect")
