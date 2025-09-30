class HCN:
    def __init__(self, canhA:str=0, canhB:int=0):
        self.canhA = canhA
        self.canhB = canhB
    def nhap(self):
        self.canhA = str(input("Nhập cạnh A: "))
        self.canhB = int(input("Nhập cạnh B: "))
    def chu_vi(self):
        return 2*(self.canhA+self.canhB)
    def dien_tich(self):
        return self.canhA*self.canhB
    def display(self):
        print(f"Độ dài cạnh A={self.canhA} Độ dài cạnh B={self.canhB}")
        print("Chu vi HCN: ",self.chu_vi())
        print("Diện tích HCN: ",self.dien_tich())
hcn = HCN()
hcn.nhap()
hcn.display()

