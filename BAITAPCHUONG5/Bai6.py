def NegativeNumberInStrings(s):
    import re
    nums = re.findall(r'-\d+', s)
    if nums:
        print("Các số nguyên âm trong chuỗi là:", ", ".join(nums))
    else:
        print("Không có số nguyên âm nào trong chuỗi.")


string=input("Nhap chuỗi: ")
NegativeNumberInStrings(string)
