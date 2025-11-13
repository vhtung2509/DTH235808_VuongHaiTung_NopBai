from SinhVien import SinhVien
class LopHoc:
    def __init__(self, maLop, tenLop):
        self.maLop = maLop
        self.tenLop = tenLop
        self.sinhVienList = []

    def themSinhVien(self, sinhVien):
        self.sinhVienList.append(sinhVien)

    def to_dict(self):
        return {
            'maLop': self.maLop,
            'tenLop': self.tenLop,
            'sinhVienList': [sv.to_dict() for sv in self.sinhVienList]
        }

    @classmethod
    def from_dict(cls, data):
        lopHoc = cls(
            maLop=data['maLop'],
            tenLop=data['tenLop']
        )
        lopHoc.sinhVienList = [SinhVien.from_dict(sv_data) for sv_data in data['sinhVienList']]
        return lopHoc