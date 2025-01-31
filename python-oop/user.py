class User:
    def __init__(self, name, email,age):
        self.name = name
        self.__email = email
        self.age = age
    def user_information(self):
        return f"user info: name:{self.name}, email:{self.__email}, age: {self.age}"
    def update_email(self, new_email):
        self.__email = new_email
        return f"email updated to {new_email}"
    def check_eligibility(self):
        if self.age >= 18:
            return f"{self.name} you are eligible for an ID"
        else:
            return f"{self.name} you are not eligible for an ID"

# creating a user object   
user1 =  User("brian", "brian@gmail.com", 25) 
user2 = User("amon", "amon@gmail.com", 15)  

# display user information
print(user1.user_information())

# updating the user email
print(user1.update_email("yoh@gmail.com"))

user1.__email = "tycoon@gmail.com"
print(user1.__email)

# check eligibility
print(user1.check_eligibility())
print(user2.check_eligibility())