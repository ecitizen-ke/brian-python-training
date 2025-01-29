from datetime import datetime  # Import datetime module


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email  # Private email field
        self.password = password

    def say_hi_to_user(self, user):
        print(f"sending message to {user.username}: Hi {
        user.username}, it's {self.username}")

    # Method to access the email field
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email

    # Method to modify the email field
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email  # Set to the private _email field
        else:
            print("Invalid email format!")


# Creating two User objects
user1 = User("Tom", "Tom@gmail.com", "123")
user2 = User("caleb", "caleb@gmail.com", "1334")

# Sending a message to user2 from user1
user1.say_hi_to_user(user2)

# Accessing email via getter method
print(user1.get_email())  # Prints email and the time it was accessed

# Trying to set an invalid email
user1.set_email("tyuioty.com")  # Invalid email
print(user1.get_email())  # Email won't be changed, still the original one

# Setting a valid email
user1.set_email("newemail@example.com")
print(user1.get_email())  # Email should be updated
