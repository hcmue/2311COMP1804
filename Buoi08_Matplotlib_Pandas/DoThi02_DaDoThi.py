import matplotlib.pyplot as plt

# Nếu có nhiều đồ thị thì dùng subplot và đánh vị trí 
# .subplot(số_dòng, số_cột, thứ_tự_ô)

plt.subplot(2, 3, 1)
plt.plot([1,2,3,4], [1,4,6,9], "mo-")
plt.title("Biểu đồ giá dầu")
plt.xlabel("lít")
plt.ylabel("$ (USD)")
plt.grid()

plt.subplot(2, 3, 6)
plt.plot([1,2,3.9], [100, 190, 230], "m^-")
plt.title("Biểu đồ giá xăng")
plt.xlabel("lít")
plt.ylabel("đ")
plt.grid()

plt.show()
