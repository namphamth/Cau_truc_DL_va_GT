import random

def san_sinh_mang_tang_dan(n):
    mang =[] 
    
    so_dau_tien = random.randint(-100,100)
    mang.append(so_dau_tien)
    
    for i in range(1,n):
        # khởi đđộng từ 1 vì 0 là vị trí số đầu tiên
        tang = random.randint(1,10)
        # đây là số sau có đơn vị lớn hơn tối đa là 10 đơn vị
        so = mang[i-1] + tang  
        # tức là số sau bằng số trước nó cộng với số sau tăng lên 1 đến 10 đơn vị
        
        mang.append(so)
    return mang 

# Thuật toán tìm kiếm nhị phân là thuật toán tìm kiếm trong 1 tập dữ liệu được sắp xếp thuật toán này giảm nửa kích thước của tập dữ liệu mỗi lần timf kiếm dựa trên so sánh giá trị ở giữa
def tim_nhi_phan(mang,x):
    trai = 0
    phai = len(mang) - 1
    
    while trai <= phai :
        giua = (trai + phai) // 2 # chia lấy phaan nguyên
        if mang[giua] == x:
            return giua
        if x< mang[giua] :
            phai = giua -1
        else :
            trai = giua + 1
        
    return -1


def main() :
    mang = san_sinh_mang_tang_dan(24)
    print(mang)
    
    x = int(input('Nhập vào giá trị cần tìm :'))
    
    vitri = tim_nhi_phan(mang,x)
    
    if vitri != -1 :
        print(f" giá trị {x} được tìm thấy tại vị trí {vitri}")
    else :
        print(f" giá trị {x} kh được tìm thấy  ở vị trí nào")
        
        
if __name__=="__main__" :
    main()
        