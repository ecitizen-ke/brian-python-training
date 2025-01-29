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



        






