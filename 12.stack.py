# định nghĩa danh sách bằng list
class Stack :
    def __init__(self):
        self.danh_sach = []
        
    def la_rong(self):
        return len(self.danh_sach) == 0
    
    def __str__(self):
        kq = 'Ngăn xếp ['
        stt = 0
        for x in self.danh_sach:
            stt = stt +1
            if stt == 1 :
               kq = kq + str(x)# phần tử đầu tiên kh có dấu nối
            else:
                kq = kq + '->' + str(x)# từ phần tử thứ 2 sẽ có dấu nối
                
        kq = kq + ']'
        return kq
        
    def day_vao(self , giatri):
       self.danh_sach.insert(0,giatri) # số 0 ở đây là thêm vào đầu
       
    
    def lay_ra(self):
        if self.la_rong():
            return None
        else :
            return self.danh_sach.pop(0)# lấy ra từ đầu khi thêm số 0 vào nếu kh nó sẽ mặc định lấy ra từ cuối
        pass
    
    
if __name__ == '__main__':
    ngan_xep = Stack()
    print(ngan_xep)
    print('-----Đẩy Vào-----')
    for i in range(1,6):
        print(f'* Đẩy Vào{i}')
        ngan_xep.day_vao(i)
        print(ngan_xep)
        
        
    print('-----Lấy Ra----')
    while not ngan_xep.la_rong():
        gt = ngan_xep.lay_ra()
        print(f'* Lấy Ra -> {gt}')
        