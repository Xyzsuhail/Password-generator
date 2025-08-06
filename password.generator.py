# Create a random password generator

# First import the modules
import random
import string

#Ask the user for the password len
pass_len = int(input("Enter the length of the password you want: ")) 

#Ask the user what to include
use_letters = input("Do you want letters? ").lower() #(yes or no)
use_numbers = input("Do you want numbers? ").lower() #(yes or no)
use_special_characters = input("Do you want to add special characters? ").lower() #(yes or no)

#Building a variable to store the characters
characters = ""

if(use_letters == "yes"):
    characters += string.ascii_letters
if(use_numbers == "yes"):
    characters += string.digits 
if(use_special_characters == "yes"):
    characters += string.punctuation

#Generate a random password
password = ""

for i in range(pass_len):
    password += random.choice(characters)

#to handle errors
if characters == "":
    print("You must select atleast one category!")
else:
    print(f"Your new password is: {password}")    