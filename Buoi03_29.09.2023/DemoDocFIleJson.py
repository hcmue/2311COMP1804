import json

try:
    with open("student.json", "r", encoding="utf-8") as myfile:
        data = json.load(myfile)
       
    print("DATA", data)
    
    tong_so_tc = 0
    tong_diem = 0
    for mon in data["mon_hoc"]:
        tong_so_tc += mon["so_tc"]
        tong_diem += mon["so_tc"] * mon["diem"]
    diem_tb = tong_diem / tong_so_tc
    
    # Cập nhật lại
    data["diem_tb"] = diem_tb
    with open("student.json", "w", encoding="utf-8") as myfile:
        data = json.dump(data, myfile, indent=4)
except Exception as ex:
    print(ex)