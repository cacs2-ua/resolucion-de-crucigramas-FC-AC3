from main import *

def main():
    class ClassA:
        def __init__(self, age):
            self._age = age
        
        def get_age(self):
            return self._age
    
    classA_instance = ClassA(25)
    my_age = classA_instance.get_age()

    print(f"my_age: {my_age}, Memory address: {id(my_age)}")
    print(f"classA_instance.get_age(): {classA_instance.get_age()}, Memory address: {id(classA_instance.get_age())}")
    
    
    my_age = 30
    print(f"my_age: {my_age}, Memory address: {id(my_age)}")
    print(f"classA_instance.get_age(): {classA_instance.get_age()}, Memory address: {id(classA_instance.get_age())}")

if __name__=="__main__":
    main()