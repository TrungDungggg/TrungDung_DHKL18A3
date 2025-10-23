import json
from datetime import datetime
def nhap_giao_dich():
    ma_gd = input("Nhập mã giao dịch: ")
    ngay_gd = input("Nhập ngày giao dịch (vd:22/10/2025):")
    loai_gd = input("Nhập loại giao dịch:")
    so_tien_gd = float(input("Nhập số tiền giao dịch:"))
    mo_ta_gd = input("Nhập mô tả:")
    return {
        "loai_gd": loai_gd,
        "ma_gd":ma_gd,
        "ngay_gd":ngay_gd,
        "so_tien_gd":so_tien_gd,
        "mo_ta_gd":mo_ta_gd
    }
def main():
    ds_giao_dich = []
    print("===QUẢN LÝ GIAO DỊCH===")
    while True:
        gd = nhap_giao_dich()
        ds_giao_dich.append(gd)
        tiep = input("Bạn có muốn nhập thêm giao dịch kh? (yes/no):").lower()
        if tiep == "no":
            break
    print("===DANH SÁCH GIAO DỊCH===")
    for gd in ds_giao_dich:
        print(f"{gd['ma_gd']} | {gd['loai_gd']} | {gd['ngay_gd']} | {gd['so_tien_gd']} | {gd['mo_ta_gd']}")
        tiep_tuc = input("Bạn có muốn ghi vào tệp JSON không?(1: có, 0: không):")
        if tiep_tuc == '1':
            now = datetime.now()
            ten_file = now.strftime("%Y-%m-%d-%H-%M-%S.json")
            duong_dan = r"D:\18A3DHKL\BTVN\chuong2"
            duong_dan_f = f"{duong_dan}\\{ten_file}"
            with open(duong_dan_f, "w", encoding="utf-8") as f:
                        json.dump(ds_giao_dich, f, ensure_ascii=False, indent=4)
            print(f"Dữ liệu đã được ghi vào tập tin '{duong_dan_f}' thành công!")
        else:
            print(" Không ghi dữ liệu. Kết thúc chương trình.")
if __name__ == "__main__":
    main()
