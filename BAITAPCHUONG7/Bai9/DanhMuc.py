from SanPham import SanPham
class DanhMuc:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten
        self.sanPhamList = []

    def themSanPham(self, sanPham):
        self.sanPhamList.append(sanPham)
    def toDict(self):
        return {
            'ma': self.ma,
            'ten': self.ten,
            'sanPhamList': [sp.toDict() for sp in self.sanPhamList]
        }
    @staticmethod
    def fromDict(data):
        danhMuc = DanhMuc(data['ma'], data['ten'])
        danhMuc.sanPhamList = [SanPham.fromDict(spData) for spData in data['sanPhamList']]
        return danhMuc
    