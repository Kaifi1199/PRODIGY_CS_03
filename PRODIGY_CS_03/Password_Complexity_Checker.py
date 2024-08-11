import re
import msvcrt

def get_password():
    password = ""
    print("\nEnter your Password: ", end="", flush=True)
    while True:
        ch = msvcrt.getch()
        if ch in {b'\r', b'\n'}:
            print()
            break
        
        elif ch == b'\x08':
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += ch.decode("utf-8")
            print("*", end="", flush=True)
    return password

def password_checker(password):
    strength = 0
    feedback = []
    
    if len(password) < 8:
        feedback.append("Password is too short! It should be at least 8 characters long.")
    elif len(password) > 12:
        strength += 1
        feedback.append("Password is strong.")
        
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password must contain at least one uppercase character.")
        
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password must contain at least one lowercase character.")
        
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password must contain at least one number.")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password must contain at least one special character.")
        
    if strength < 2:
        return "Weak Password", feedback
    if strength < 4:
        return "Moderate Password", feedback
    else:
        return "Strong Password", feedback
    
def main():
    print("Welcome to Password Complexity Checker!")
    print("Press q to quit at any time: ")
    while True:
        password = get_password()
        
        if password.lower() == 'q':
            print("\n\t\t|---------------------------------------------------------------|")
            print("\t\t\tThankyou for using the Password Complexity Checker!")
            print("\t\t|---------------------------------------------------------------|\n")
            break
        
        print(f"\nYour Password: {password}")
        
        strength, feedback = password_checker(password)
        print(f"\nPassword Strength: {strength}")
        print("\nFeedback: \n")
        
        for item in feedback:
            print(f"- {item}")
            
if __name__ == "__main__":
    main()