class Dog:
    DogCount = 0 
    def __init__(self,name,age,size,color):
        self.name = name
        self.age = age
        self.size = size
        self.color = color
    def __del__(self):
        print("Đã xóa con chó")
obj = Dog("Bull", 2,"Small","Vàng")
del obj
        