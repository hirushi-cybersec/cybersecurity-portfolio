green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
reset = '\033[0m'

common_passwords = ['password', '123456', '111111','000000','abc123', 'password123']

password = input("Enter a password: ")

if password.lower() in common_passwords:
    print("\033[91mstrength:very weak\033[0m")
    print("Reason:This is a very common password.Hackers try these first!")
else:
    score = 0
    missing=[]

    if len(password) >= 8:
        score += 1
    else: missing.append("at least 8 characters")

    if any(x.isupper() for x in password):
        score += 1
    else:
        missing.append("an uppercase letter A-Z")

    if any(x.islower() for x in password):
        score += 1
    else:
        missing.append("an lowercase letter a-z")

    if any(x.isdigit() for x in password):
        score += 1
    else:
        missing.append("a number 0-9")

    if any(x in "!@#$%^&*" for x in password):
        score += 1
    else:
        missing.append("a symbol !@#$%^&*")

    if score >= 4:
        print(f"{green}Strength: Strong")
    elif score == 3:
        print(f"{yellow}Strength: Medium")
    else:
        print(f"{red}Strength: Weak")
        print("missing:",",".join(missing))
    print(f"{reset}")

input("press enter to exit")
