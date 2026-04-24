def register_EIV():
    username_EIV = input("Enter username: ")
    password_EIV = input("Enter password: ")
    with open("users.txt", "a") as file_EIV:
        file_EIV.write(username_EIV + "," + password_EIV + "\n")
    print("Registration successful!")

def login_EIV():
    username_EIV = input("Enter username: ")
    password_EIV = input("Enter password: ")
    try:
        with open("users.txt", "r") as file_EIV:
            for line_EIV in file_EIV:
                stored_user_EIV, stored_pass_EIV = line_EIV.strip().split(",")
                if username_EIV == stored_user_EIV and password_EIV == stored_pass_EIV:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users registered yet!")

def main_EIV():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice_EIV = input("Enter choice: ")
        
        if choice_EIV == "1":
            register_EIV()
        elif choice_EIV == "2":
            login_EIV()
        elif choice_EIV == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_EIV()
