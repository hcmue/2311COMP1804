arr = ["Cam", 23, True, "Đào"]
print(arr)
print(arr[2]) # True
print(arr[-4], arr[-1]) # Cam

# Thêm 1 phần tử vào list
arr.append("Lê")
print(arr)

mang = ["Toán", "Lý", "Hóa"]
print(", ".join(mang)) #Nối mảng chuỗi thành chuỗi
# Kiểm tra 1 phần tử có trong mảng ko: in
if "Mận" in arr:
    print("Có")

print("Có" if "Mận" in arr else "Không")

# Xóa remove(gia_tri)