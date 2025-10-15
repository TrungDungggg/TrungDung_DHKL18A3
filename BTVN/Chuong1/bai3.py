class Phan_so():
    def __init__(self,tu_so:int,mau_so:int):
        self.tu_so = tu_so
        self.mau_so = mau_so
    def kiem_tra(self):
        if self.mau_so == 0:
            raise ValueError("Mẫu số phải khác 0")
    def display(self):
        print(f"{self.tu_so}/{self.mau_so}")
try:
    ps1 = Phan_so(3, 4)      
    ps1.display()
    ps1.kiem_tra()
    ps2 = Phan_so(5, 0)      
    ps2.kiem_tra()
    ps2.display()
except ValueError as e:
    print("Lỗi ps2 :", e)
    