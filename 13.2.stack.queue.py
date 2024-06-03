# hàng đợi là mô tả hsngf đợi hoạt động theo nguyên tắc vào trước ra trước

from dslk import DS_LienKet

class hang_doi:
    def __init__(self):
        self.danh_sach = DS_LienKet()
        
    def __str__(self):
        kq = 'Hàng Đợi ['
        kq = kq + str(self.danh_sach)
        kq = kq +']'
        return kq
        
    def la_rong(self):
        return self.danh_sach.dau == None
    
    def xep_hang(self,giatri):
        self.danh_sach.them_duoi(giatri)
    
    def ra_hang(self):
        if self.la_rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()
            self.danh_sach.xoa_dau()
            return kq
        
if __name__ == '__main__':
    hd = hang_doi()
    print(hd)
    
    print('----Hàng Đợi---')
    for x in range(1,6):
        print(f'* xếp hàng {x}')
        hd.xep_hang(x)
        print(hd)
        
    print('----Ra Hàng----')
    while not hd.la_rong() :
        rh = hd.ra_hang()
        print(f'* ra hàng {rh}')
        print(hd)