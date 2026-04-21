#bai 13
import re
def chuan_hoa_chuoi(s):
# Xoa Khoang trang dau cuoi
    s = s.strip()
#Xoa khoang trang thua
    s = re.sub(r'\s+', ' ', s)
#Xoa khoang tran cham phay
    s = re.sub(r'\s([.,])', r'\1 ', s)
    return s

#Nhap
text = """   Quê hương   là  chùm khế  ngọt .
   Cho con trèo hái mỗi ngày .   """
print(chuan_hoa_chuoi(text))