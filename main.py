import random

chars = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%^&*()"


while 1:
    print("Note: recommended minimum password length is 8 characters")
    password_len = int(input("What length would you like your password to be :"))
    password_count = int(input("How many passwords would you like: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password: ", password)
