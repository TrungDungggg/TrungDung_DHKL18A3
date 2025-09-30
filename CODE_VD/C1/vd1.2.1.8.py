class Dog:
    def __init__(self,name,size,age,color):
        self.name = name
        self.size = size
        self.age = age
        self.color = color 
    def display_detailes(self):
        print("Name:%s,size:%s,age:%d,color:%s"%(self.name,self.size,self.age,self.color))
bull = Dog("Dom","large",2,"Yellow")
print("Base clases of Dog: ",Dog.__base__)
print(bull.__doc__)
print(bull.__dict__)
print(bull.__module__)
print(Dog.__name__)