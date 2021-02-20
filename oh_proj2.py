"""
Write a program that creates 2 variables to store the username "Joe"
and the password "p@ssw0rd"

Prompt the user up to 3 times for a username.
If the username is not "Joe",
 print a message to the user that says "Invalid user."
 and continue prompting for a correct username until "Joe" is
 entered or until the maximum number of tries (3) has been exceeded.

If the maximum number of username attempts is exceeded,
print "Maximum number of attempts exceeded, exiting."
If "Joe" is entered on or before the third attempt,
prompt the user for a password ("Enter password:")
until a valid password is entered.  Once you receive a
valid password, print "Welcome to TikTok!"

Once complete, test your program with various inputs that exercise each
logical path through your code.
"""

usr = input("Please enter username: ")
attempt = 1
while usr != "Joe":
    print("Invalid username")
    attempt += 1
    usr = input("Please enter username: ")
    if attempt == 4:
        print("Exceeded max login attempts, exiting")
        break
else:
    password = input("Please enter password: ")
    while password != "p@ssw0rd":
        print("Please try again")
        password = input("Please enter password: ")
    print("Welcome to TikTok!")
