# -1  0  1  2  3  4  5   6
#     6  5  2  4  3  10 (8)
#  i
#     j





import random

def san_sinh_nn(n):
    mang=[]
    for i in range(n):
        so_nn = random.randint(0,100)
        mang.append(so_nn)
    return mang

def phan_vung(mang,duoi,tren):
    i = duoi - 1 # chỉ mục của phần tử nhỏ hơn mốc
    moc = mang[tren] # pivot giá trị mốc ở cuối dãy số là số 8
    # đưa lần lượt các phần tử nhỏ hơn mốc vế trên
    for j in range(duoi, tren):# j chạy từ 6 => 8 
        if mang[j] < moc:# so sánh tất các số với mốc là 8
            i = i+1
            mang[i] , mang[j] = mang[j] , mang[i]
        
    mang[i+1] , mang[tren] = mang[tren] , mang[i+1] 
    return i + 1

def sap_xep_nhanh(mang,duoi,tren):
    if duoi < tren:
        vitri = phan_vung(mang,duoi,tren)
        sap_xep_nhanh(mang,duoi,vitri-1)
        sap_xep_nhanh(mang,vitri+1,tren)
        

def main():
    mang=san_sinh_nn(10)
    print("mảng bđ :\n", mang)
    sap_xep_nhanh(mang, 0 , len(mang)-1)
    print("mảng sau :\n", mang)
    
if __name__=='__main__':
    main()