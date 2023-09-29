sv = {
    "ma_sv": "48.01.104.023",
    "ho_ten": "Tèo",
    "gioi_tinh": True,
    "tuoi": 21,
    "diem_tb": 8.6,
    "mon_hoc": [
        {
            "ma_mon": "COMP1084", "ten_mon": "Thương mại Điện tử",
            "so_tc": 3, "diem": 8.9
        },
        {
            "ma_mon": "COMP1804", "ten_mon": "Lập trình Python",
            "so_tc": 3, "diem": 9.8
        }
    ]
}
ma_mon = input("Mã môn: ")
ten_mon = input("Tên môn: ")
so_tc = int(input("Số tín chỉ: "))
diem = float(input("Điểm HP: "))
mon_moi = {
    "ma_mon": ma_mon, "ten_mon": ten_mon, "so_tc": so_tc, "diem": diem
}
sv["mon_hoc"].append(mon_moi)

import json
json_str = json.dumps(sv, indent=4)
print(json_str)

with open("student.json", "w") as myfile:
    json.dump(sv, myfile, indent=4)