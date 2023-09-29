# Nhớ cài thư viện requests
import requests

# Gọi api
r = requests.get("https://thongtindoanhnghiep.co/api/city")
print(r)

print('STATUS:', r.status_code)
print(r.text)

# API đã trả về dạng JSON nên dùng hàm json() lấy
data_response = r.json()
print(data_response)

'''Bài tập
Sử dụng API được cung cấp ở trang https://thongtindoanhnghiep.co/rest-api
Lấy và tổ chức thông tinh tỉnh/thành, quận/huyện và lưu file json
'''