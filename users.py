from data import users

def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username taken.")
        return None
    password = input("Create password: ")
    users[username] = {'password': password, 'loyalty': 0}
    print("Registration successful.")
    return username

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]['password'] == password:
        print("Login successful.")
        return username
    print("Invalid credentials.")
    return None
