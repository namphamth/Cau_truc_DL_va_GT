from dslk import DS_LienKet

class stack :
    def __init__(self):
        self.danhsach = DS_LienKet()
    def la_rong(self):
        return self.danhsach.dau == None
    
    def __str__(self):
        kq = 'ngan xep ['
        kq = kq + str(self.danhsach)
        kq = kq +']'
        return kq
    
    def day_vao(self,giatri):
        self.danhsach.them_dau(giatri)
        
    def lay_ra(self):
        if self.la_rong() :
            return None
        else :
            kq = self.danhsach.lay_dau()
            self.danhsach.xoa_dau()
            return kq
        
if __name__ == "__main__":
    st = stack()
    print(st)
    print('-----Đẩy vào-----')
    for i in range(1,6):
        print(f' đẩy vào {i}')
        st.day_vao(i)
        print(st)
    
    print('----lấy ra----')
    while not st.la_rong():
        gt = st.lay_ra()
        print(f'* lấy ra -> {gt}')
        print(st)