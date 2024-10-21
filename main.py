from encryptor import hash_password, checked_password
from orm import add_user, get_user_by_name

def register_user():
    user_name = input("Enter your user name:" )
    password = input("Enter your password:" )

    hashed_password = hash_password(password)

    user = add_user(user_name, hashed_password)
    if user:
        print(f"User {user.user_name} succesfully registred with id {user.id}.")
        print(f"User profile: Name: {user.user_name}, Hashed password: {user.password}")
    else:
        print("User registred not succesfully.")

def login_user():
    user_name = input("Enter your user name:" )
    password = input("Enter your password:" )

    user = get_user_by_name(user_name)
    
    if not user:
        print("User not found.")
        return
    
    if checked_password(password, user.password):
        print("Login successful!")
    else:
        print("Invalid password.")

register_user()
login_user()