import csv

STUDENT_DATA_CSV = "student_data.csv"
with open(STUDENT_DATA_CSV, "w", encoding="UTF8") as myfile:
    svw = csv.writer(myfile, delimiter=',', 
			quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # Ghi từng dòng
    svw.writerow(["Mã số sv",	"Họ lót",	"Tên",	"Giới tính", 
            "Ngày sinh",	"Nơi sinh",	"Chuẩn xét",
            "Điểm TB Tích lũy",	"Số TCBB",	"Số TCTC",	"Số TC học lại"])

    svw.writerow(["42.01.104.121", "TRẦN THANH", "PHƯƠNG",	"TRUE",
    	"02/09/1997",	"Tp. Hồ Chí Minh",	"Công nghệ thông tin - Công nghệ phần mềm và hệ thống thông tin",	2.77,	80,	42,	34])

