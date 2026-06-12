import re

password = input("Senha: ")

score = 0

#Checks if the password is longer than 8 digits
if len(password) >= 8:
    score += 1

#Checks if the password has capital letters
if re.search("[A-Z]", password):
    score += 1

#Checks if the password has numbers on it
if re.search("[0-9]", password):
    score += 1

#Checks if there's a special character in the password
if re.search("[@!#$%]", password):
    score += 1
    
    
if score == 4:
    print("Strong password")
elif score >= 2:
    print("Medium password")
else:
    print("Weak password")
    
    
    
    
