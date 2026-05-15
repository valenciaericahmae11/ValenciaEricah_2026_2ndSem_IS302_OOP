def load_users(filepath="users.txt"):
    users_EMIV = {}
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                raise ValueError("Invalid user data format")
            username = parts[0].strip()
            password = parts[1].strip()
            users_EMIV[username] = password
    return users_EMIV


def main():
    try:
        users_EMIV = load_users("users.txt")
    except FileNotFoundError:
        print("User credentials file not found.")
        return
    except ValueError as err:
        print("Error loading users:", err)
        return

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty.")
        return

    if username in users_EMIV and users_EMIV[username] == password:
        print("Login successful.")
    else:
        print("Login failed. Check username and password.")


if __name__ == "__main__":
    main()