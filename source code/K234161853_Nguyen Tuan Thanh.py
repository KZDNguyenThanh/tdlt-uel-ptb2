def tinh_npv(dautu, dukien, chietkhau,thoigian):
    npv = 0
    for i in range(1,thoigian+1):
        npv += (dukien/((1+chietkhau)**i))
    npv -= dautu
    return npv
def phantich_npv(npv):
    if npv > 0:
        return "NPV duong, du an co kha nang sinh loi va nen duoc thuc hien."
    elif npv == 0:
        return "NPV bang 0, du an hoa von va chi nen chon neu khong co phuong an tot hon."
    else:
        return "NPV am, du an co kha nang lo va KHONG NEN duoc thuc hien."
dautu = float(input("Nhap so tien dau tu: "))
chietkhau = float(input("Nhap ti le chiet khau (Vi du 10% thi nhap 0.1): "))
thoigian = int(input("Nhap thoi gian dau tu du kien: "))
dukien = float(input("Nhap doanh thu du kien: "))
npv = tinh_npv(dautu, dukien, chietkhau,thoigian)
npv = round(npv,2)
analysis = phantich_npv(npv)
print(f"Giá trị NPV là: {npv}")
print(analysis)
