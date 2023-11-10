import pandas as pd
import os
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales2019_1.csv")
print(df)

# Task: Nối 12 file (12 tháng vô chung 1 dataframe)
# khi nối thêm cột Month (01 --> 12)

# Tiền xử lý dữ liệu
# Config kiểu dữ liệu của cột
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], downcast='integer')
df['Price Each'] = pd.to_numeric(df['Price Each'], downcast='float')
df['Total'] = df['Quantity Ordered'] * df['Price Each']

# print(df)
cot_ve = df.pop('Sales')
plt.bar(x=['141234', '141235'], height=[123, 454]) # Hard code
plt.show()

