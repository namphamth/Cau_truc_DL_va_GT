# cây có nhiều nút nút gốc và tối đa 2 nút con cùng nhiều lá (trái thì thêm số nhỏ hơn, phải thì thêm nút lớn hơn)
class Nut :
    
    def __init__(self , khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None
     
    def chen(self , khoa):
        if self is None:
            nut = Nut(khoa)   
            self = nut
            return
        
        if khoa < self.khoa:
            if self.trai == None :
                self.trai = Nut(khoa)
            else:
                self.trai.chen(khoa)
                
        elif khoa > self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)
            else :
                self.phai.chen(khoa)
                
        else :
            print(f' bị trùng khoá {khoa}')
            
class Caynhiphan_timkiem :
    def __init__(self , khoa = None):
        if khoa == None :
            