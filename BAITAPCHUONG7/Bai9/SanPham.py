class SanPham:
    def __init__(self, ma, ten, donGia):
        self.ma = ma
        self.ten = ten
        self.donGia = donGia

    def toDict(self):
        return {
            'ma': self.ma,
            'ten': self.ten,
            'donGia': self.donGia
        }

    @staticmethod
    def fromDict(data):
        return SanPham(data['ma'], data['ten'], data['donGia'])
    
