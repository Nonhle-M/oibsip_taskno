# password generator
import random 
import string
character_set = string.ascii_letters + string.digits + string.punctuation 
password_length = int(input("Enter the length of the password: "))
generated_password = ''.join(random.choices(character_set, k=password_length))
print('Your password :',generated_password)
