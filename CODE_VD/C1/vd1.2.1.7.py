class Dog:
    DogCount = 0 # thuộc tính của lớp 
    def __init__(self,name,size,age,color):
        self.name = name
        self.size = size
        self.age = age
        self.color = color
bull = Dog("Dom","Large",2,"Red")
print(getattr(bull,'name'))
setattr(bull, "age",3)
print(getattr(bull,'age'))
print(hasattr(bull, 'large',"small"))
delattr(bull, 'age')
print(bull.age)