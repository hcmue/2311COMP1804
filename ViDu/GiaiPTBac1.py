from tkinter import *
from tkinter import messagebox

def mouse_in_ok(e):
	cmd_ok['background'] = 'yellow'

def mouse_out_ok(e):
	cmd_ok['background'] = 'SystemButtonFace'

def mouse_in_exit(e):
	cmd_exit['background'] = 'red'

def mouse_out_exit(e):
	cmd_exit['background'] = 'SystemButtonFace'

wd=Tk()
wd.geometry("500x300")
wd.title("Giải phương trình bậc nhất")
# C1- Đặt icon cùng thư mục với tệp .py
# wd.iconbitmap('ngoccs.ico')

# C2- Đặt icon cùng thư mục với tệp .py
#wd.call('wm', 'iconphoto', wd._w, PhotoImage(file='ngoccs.png'))

# C3-Đặt icon lên cửa sổ
#wd.iconphoto(False, PhotoImage(file='ngoccs.png')) 

# Nhãn thông báo
tb=Label(wd,text="CHƯƠNG TRÌNH GIẢI PHƯƠNG TRÌNH BẬC NHẤT",font=("cambaria",12,"bold"),fg="blue")
tb.place(x=70,y=30)

# Nhãn hệ số a và textbox a
lb_a=Label(wd,text="Nhập số a:",font=("consolas",11),fg="red")
lb_a.place(x=100,y=70)
txt_a=Entry(wd,width=20,bd=1); 
txt_a.place(x=200,y=70)


# Nhãn hệ số b và textbox b
lb_b=Label(wd,text="Nhập số b:",font=("consolas",11),fg="red")
lb_b.place(x=100,y=100)
txt_b=Entry(wd,width=20,bd=1); 
txt_b.place(x=200,y=100)


kq=""
bo=""
lb_kq=Label(wd,text="",font=("cambaria",12,"bold"),fg="blue")
lb=Label(wd,text="",font=("cambaria",10,"bold"),fg="blue")


#Hàm tính giá trị
def gpt():

		try:
			a=float(txt_a.get())
			b=float(txt_b.get())
			if a!=0:
				kq="PT có ngiệm x= "+str(-b/a)
			elif b!=0:
				kq="PT vô nghiệm!"
			else:
				kq="PT vô số nghiệm!"
			lb_kq.config(text=kq)
		
			if b>=0: bo=" + " + str(b)
			if b<0: bo=str(b)

			lb.config(text="Phương trình: "+str(a)+"X "+ bo +" = 0")
			
		except: messagebox.showwarning("Cảnh báo","Xin lỗi! Hệ số không hợp lệ")
def thoat():
	messagebox.showinfo("Thông báo","Cảm ơn bạn!")
	wd.destroy()

cmd_ok=Button(wd,text="Giải PT",width=8,font=("tahoma",10),fg="blue",command= gpt)
cmd_ok.place(x=250,y=230)


cmd_exit=Button(wd,text="Thoát",width=8,font=("tahoma",10),fg="blue",command= thoat)
cmd_exit.place(x=150,y=230)

lb_kq.place(x=120,y=170)

lb.place(x=150,y=125)

cmd_ok.bind("<Enter>", mouse_in_ok)
cmd_ok.bind("<Leave>", mouse_out_ok)

cmd_exit.bind("<Enter>", mouse_in_exit)
cmd_exit.bind("<Leave>", mouse_out_exit)

wd.mainloop()