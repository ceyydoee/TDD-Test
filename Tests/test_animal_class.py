
import unittest
from animal import animal

class test_animal(unittest.TestCase):
    def test_animal_cat(self):
        animal1=animal()

        if animal1.type == "cat":
            self.assertEqual(animal1.name , "seymore")
            if animal1.name!="seymore":
                print(animal1.name)
        pass

    
    def test_animal_dog(self):
        animal2 =animal()

        if animal2.type=="dog":
            self.assertEqual(animal2.namle,"spot")
            if animal2.name!="spot":
                print(animal2.name)
    
    def speak(self):
        for size in animal :
            if size == "small" and type == "cat":
                    print("meow")
            else: print("MEOW")

    def speak(self):
        for size in animal:
            if size == "small" and type =="dog":
                        print ("bow bow")
            elif size =="medium" and type == "dog":
                        print("ruff ruff")
            else: 
                        print("arf arf")

    def describ(self):
        for age in animal:
            if age <10:
                print("young")
            else:
                print("old")




        pass
    





    