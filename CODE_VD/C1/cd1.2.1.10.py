class Dog:
    DogCount = 0

    def __init__(self, name, size, age, color):
        self.name = name
        self.size = size
        self.age = age
        self.color = color 

    @classmethod
    def CreateDog(cls, name, size, age, color):
        cls.DogCount = cls.DogCount + 1
        return cls(name, size, age, color)

    @classmethod
    def get_dog_count(cls):
        return cls.DogCount


obj = Dog.CreateDog("bull", "large", 2, "yellow")
print("So luong doi tuong Dog da duoc tao: ", Dog.get_dog_count())

obj2 = Dog.CreateDog("poodle", "small", 1, "white")
print("So luong doi tuong Dog da duoc tao: ", Dog.get_dog_count())
