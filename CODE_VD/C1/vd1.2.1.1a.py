class Nhan_vien:
    def __init__(self,id:int, name:str, age:int ):
        self.id = id 
        self.name = name 
        self.age = age
    def display(self):
        print(f"ID: {self.id},Tên: {self.name},Tuổi: {self.age}")
nv1 = Nhan_vien(10, "Nguyen Van A", "20")
nv1.display()