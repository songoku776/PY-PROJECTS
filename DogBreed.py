# lesson 22 Dog Breed
class Dog:
    species = "Canis familiaris"

    def __init__(self, breed, color):
        self.breed = breed     
        self.color = color      
        
    def display_info(self):
        print(f"Species: {Dog.species}")
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        print("------------------------")

dog1 = Dog("Labrador Retriever", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

dog1.display_info()
dog2.display_info()
