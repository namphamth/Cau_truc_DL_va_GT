# so sánh từng phần tử phía sau với mảng đã sắp xếp dần dần
# mảng ban đầu = [1,3,2,4]
# chọn 3 làm số ss và [1] là mảng ban đầu => mảng sau là =[1,3,2,4]
#chọn 2 làm số ss với mảng [1,3] thì ta đc mảng mới là [1,2,3,4].... tiếp tục như vậy

import random

def san_sinh_so_nn(n):
    mang=[]
    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)
    return mang


def sap_xep_chen(mang):
    n = len(mang)
    for i in range(1,n):# vì 0 sẽ là phần tử manghr đầu tiên để so sánh
        tam = mang[i]
        j=i
        while j > 0 and mang[j-1] > tam:
            mang[j] =  mang[j-1]
            j = j-1
         
        mang[j] = tam
        print(i,'-',mang)
    
    
def main():
    mang = san_sinh_so_nn(10)
    print("mảng ban đầu là :\n",mang)
    sap_xep_chen(mang)
    print("mảng sau sắp xếp là :\n", mang)

if __name__ == '__main__':
    main()