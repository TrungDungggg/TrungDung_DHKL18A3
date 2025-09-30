class Dog:
    DogCount = 0 # thuộc tính của lớp 
    def __init__(self,name,size,age,color):
        self.name = name
        self.size = size
        self.age = age
        self.color = color 
    def go(self):
        print("I'm going")
    def stay(self,place):
        print("I'm saying at {}".format(place))
    def lie(self,place):
        print("I'm lying at {}".format(place))
    def bark(self):
        print("gâu")
    def eat(self,food):
        print("I'm eating{}".format(food))
# ứng dụng khởi tạo đối tượng
bull = Dog("Bull","large",2,"Yellow")
bull.lie("room")
bull.go()
                