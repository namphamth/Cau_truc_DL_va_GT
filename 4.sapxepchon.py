#sắp xếp chọn là sắp xếp vị trí nhỏ nhất ở đầu sau đó tìm min lần lượt từ các số còn lại

import random

def san_sinh_mang_nn(n):
    mang = []
    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)
    
    return mang

def sap_xep_chon(mang):
    n = len(mang)
      
    for i in range(n-1): # i = [0,n-2]
        vitrimin = i
        
        for j in range(i+1,n):# j = i+1
            if mang[vitrimin] > mang[j]:
                vitrimin = j
                
        mang[i] , mang[vitrimin] = mang[vitrimin] , mang[i]
        print(i+1 , '-' , mang)
        
def main():
    mang = san_sinh_mang_nn(11)
    print("mang ban dau:\n",mang)
    sap_xep_chon(mang)
    print('mang sau sap xep :\n',mang)


if __name__ == "__main__":
    main()
          