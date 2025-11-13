class SinhVien:
    def __init__(self, ma, ten, namSinh):
        self.ma = ma
        self.ten = ten
        self.namSinh = namSinh

    def to_dict(self):
        return {
            'ma': self.ma,
            'ten': self.ten,
            'namSinh': self.namSinh
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            ma=data['ma'],
            ten=data['ten'],
            namSinh=data['namSinh']
        )
        