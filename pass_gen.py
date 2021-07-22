import random
import string
while True:
    i = input('Please enter the lenght of the password: ')
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ",".join(random.choice(characters) for i in range((int(i))))
    print(password)
