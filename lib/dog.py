#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    def __init__(self, name="Motina", breed="Kienyeji"):
     
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"

        if breed == "Kienyeji" or breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Unknown"

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

   
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


dog = Dog()
print(dog.name)  
print(dog.breed)  

dog.name = "Buddy"
dog.breed = "Pug"
print(dog.name)
print(dog.breed)

dog.name = "Mor Kitoko"
dog.breed = "Nyadala"
