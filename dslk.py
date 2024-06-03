# Cài đặt 1 danh sách liên kết rồi ứng dụng taoh ngăn xêps và hàng đợi

class Nut :
    # Nut mô tả một nút trong danh sách gồm 1 giá trj và 1 liên kết đến nút kế tiếp trong danh sách
    def __init__(self,giatri):
        self.giatri = giatri
        self.nut_ke_tiep = None
        
class DS_LienKet:
    def __init__(self ):
        self.dau = None
        self.duoi = None
        
    def __str__(self):
        kq = ''
        stt = 0
        hien_tai = self.dau
        while hien_tai != None :
            stt = stt+1
            if stt == 1:
                kq = kq + str(hien_tai.giatri)
            else :
                kq = kq + '->' + str(hien_tai.giatri)
                
            hien_tai = hien_tai.nut_ke_tiep
        return kq
    def them_dau(self, giatri):
        nut = Nut(giatri)
        if self.dau == None:
            self.dau = nut
    
        else :
            nut.nut_ke_tiep = self.dau
            self.dau = nut 
            
            

        
    def xoa_dau(self):
        tam = self.dau
        if self.nut_ke_tiep is None:
            self.dau = None
        else :
            self.dau = self.dau.nut_ke_tiep
        del tam

def main():
    ds = DS_LienKet()
    print(ds)
    for i in range(1,6):
        print(f'them nút {i}')
        ds.them_dau(i)
        
if __name__ == '__main__':
    main()