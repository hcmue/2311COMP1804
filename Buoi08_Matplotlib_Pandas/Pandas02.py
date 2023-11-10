import pandas as pd

data = {
    "IP15": [10, 2, 23, 19, 12, 9],
    "SS Galaxy S23": [19, 21, 33, 19, 7, 9],
}

my_index = ["T1", "T2", "T3", "T4", "T5", "T6"]
my_df = pd.DataFrame(data=data, index=my_index)
print(my_df)
print(my_df.head(2)) # Lấy 2 dòng đầu
print(my_df.tail(2)) # Lấy 2 dòng đầu
print(my_df.sum())
print(my_df.min())
print(my_df.max())
print(my_df.mean())
# my_df.plot.hist()

# Export
my_df.to_excel("dulieu_banhang.xlsx")
my_df.to_json("dulieu_banhang.json")
my_df.to_csv("dulieu_banhang.csv")