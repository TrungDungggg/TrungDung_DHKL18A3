class Thi_Sinh:
    def __init__(self, hoten:str= "",diemToan:int = 0,diemHoa: int = 0,diemLy: int = 0):
        self.hoten = hoten
        self.diemToan = diemToan
        self.diemHoa = diemHoa
        self.diemLy = diemLy
    def thong_tin_ts(self):
        self.hoten = input("Nhập họ và tên thí sinh: ")
        self.diemToan = float(input("Nhập điểm Toán: "))
        self.diemHoa = float(input("Nhập điểm Hóa: "))
        self.diemLy = float(input("Nhập điểm Lý: "))
    def tong_diem(self):
        return self.diemHoa+self.diemLy+self.diemToan
    def display(self):
        print("Họ và Tên: ",self.hoten)
        print(f"Điểm Toán:{self.diemToan} ")
        print(f"Điểm Hóa:{self.diemHoa} ")    
        print(f"Điểm Lý:{self.diemLy} ")
        print(f"Tổng điểm của thí sinh:{self.tong_diem()}")
ds_thi_sinh = []
n = int(input("Nhập số lượng thí sinh: "))
for i in range(n):
    print(f"\n---Nhập thí sinh thứ {i+1}---")
    ts = Thi_Sinh()
    ts.thong_tin_ts()
    ds_thi_sinh.append(ts)
ds_trung_tuyen = [ts for ts in ds_thi_sinh if ts.tong_diem() >= 20]
ds_trung_tuyen.sort(key=lambda ts: ts.tong_diem(), reverse=True)
print("\n=====DANH SÁCH TRÚNG TUYỂN (Điểm chuẩn = 20)=====")
for ts in ds_trung_tuyen:
    ts.display()
