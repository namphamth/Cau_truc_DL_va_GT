import random

def san_sinh_mang(n):
    mang=[]
    for i in range(n):
        so_ngau_nhien= random.randint(-100,100)
        mang.append(so_ngau_nhien)
    return mang


def tim_tuyen_tinh(mang,x):
    # x là giá trị cần tìm trong mảng
    n=len(mang)# lấy tất cả các phần tử trong mảng
    for i in range(n):
        if mang[i] == x:
            # nếu giá trị i ở trong phần tử n trùng với x giá trị cần tìm thì ta trả về phần từ i
             
            return i
        
    return -1
# chạy hết mà kh trùng thì trả về giá trị kh timf thấy


def main():
    mang = san_sinh_mang(20)
    print(mang)
    
    x = int(input("nhập số giá trị cần tìm là :"))
    
    vitri = tim_tuyen_tinh(mang,x)
    
    if vitri != -1:
        print(f"giá trị {x} được tìm thấy tại trị trí {vitri}")
    else:
        print(f"không tìm thấy giá trị {x} trong mảng")


if __name__ == "__main__":
    main()
    