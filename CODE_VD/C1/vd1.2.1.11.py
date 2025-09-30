class Dog:
    DogCount = 0
    def __init__(self, name, size, age, color):
        self.name = name
        self.size = size
        self.age = age
        self.color = color 
        Dog.DogCount += 1
    @staticmethod
    def Report():
        print("TỔng số đối tượng Dog:{}".format(Dog.DogCount))
dog1 = Dog("Buddy","Medium",5,"Brown")
dog2 = Dog("Max","Small",3,"Black")
dog1.Report()