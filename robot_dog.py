
class Robot_Dog:
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val
    
    def bark(self): #class method
        print('Woof woof!')

# Main program
my_dog = Robot_Dog('Spot', 'Chihuahua')
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()