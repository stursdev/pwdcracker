#! /usr/bin/env python3

# Sam Tursunov
# This is a MD5 hash cracker program for most common passwords used
# This is strictly for educational purpuses

import hashlib
import time

start = time.clock()

pass_input = input("Please enter the MD4 Hash:\n")

# Path to a most common passwords file
path = '/users/sam/desktop/pwdcracker/pwd.txt'

try:
    # Open the password file
    pwd_file = open(path, "r")
except:
    print ("File Not Found!")
    quit()

#Set counter to 1
counter = 1

for password in pwd_file:
    # Strip new line and etc from the password
    clean_pwd = password.strip()
    # Compute the MD5 hash of the password from the file
    hashpwd = hashlib.md5(clean_pwd.encode('utf-8')).hexdigest()
    print ("Trying password number " + str(counter) + " " + str(password))
    counter += 1
    # Compare the user input MD5 hash to computed hash from the password file
    if pass_input == hashpwd:
        print ("Match Found!")
        print ("Password is: " + str(clean_pwd))
        print ("Execution time is: " + str(time.clock() - start) + " seconds")
        break
    else:
        print ("Password not found!")
