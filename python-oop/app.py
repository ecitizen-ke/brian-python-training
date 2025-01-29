class Dog:
    def __init__(self,name, breed, owner):
        self.name= name
        self.breed = breed
        self.owner = owner
    def bark (self):
        print ("whoof")    

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address= address
        self.contact_number = contact_number    
owner1 =  Owner("brian", "kapsabet", 9876556789)   
owner2 = Owner("kelvin", "eldoret", 12345)    
dog1 = Dog("sibwor", "white", owner1)
dog2 = Dog("simba", "black", owner2)
print(dog1.owner.name)   
print(dog2.breed)  

dog1.bark()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"hello, my name is {self.name} and i am {self.age} years old")    
person1 =Person("ian", 30)    
person1.greet()
person2 = Person("Bob", 40)
person2.greet()

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def say_hi_to_user(self, user):
        self.user = user    
        print(f"sending message to {user.username}: Hi {user.username}, it's {self.username}")
user1 = User("Tom", "tom@gmail.com", "123")   
user2 = User("caleb", "caleb@gmail.com", "1334") 
user1.say_hi_to_user(user2)    

# update values of a user
print(user1.email)
user1.email = "xxxx@gmail.com"
print(user1.email)


        






