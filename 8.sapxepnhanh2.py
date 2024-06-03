import random

def san_sinh_nn(n):
    mang=[]
    for i in range(n):
        so_nn = random.randint(0,100)
        mang.append(so_nn)
    return mang

def sx_nhanh(mang):
    if len(mang) >1:
        nho_hon =[]
        bang =[]
        lon_hon = []
        
        p = mang[0]# chọn mốc là số đầu tiên để so sánh
        for x in mang:
            if x < p:
                nho_hon.append(x)
            elif x==p:
                bang.append(x)
            else :
                lon_hon.append(x)
                
                
        return sx_nhanh(nho_hon) + bang + sx_nhanh(lon_hon)
    else:
        return mang
    
def main():
    mang = san_sinh_nn(5)
    print("mảng bđ :\n",mang)
    sx = sx_nhanh(mang)
    print("mảng sau :\n",sx)
    
if __name__ == '__main__':
    main()