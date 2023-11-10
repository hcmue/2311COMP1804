from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import scrolledtext

root=Tk()
root.title("Làm quen với giao diện tkinter")
root.geometry("500x300")

'''
1. Khai báo đối tượng Label trên cửa sổ
[Tên nhãn] = Label(Tên cửa sổ, text="Nội dung hiển thị")
Phương thức:
    .grid(column = (cột), row = [hàng]) //hiển thị tại vị trí cột và hàng
    .place(x=[comumn],y=[row])
[Tên nhãn].config(text=[Nội dung hiển thị]) //Gán nội dung mới cho nhãn

2. Font chữ và cỡ chữ
[Tên nhãn] = Label([Tên cửa sổ],text=["Nội dung hiển thị"],font=([Tên font],[Cỡ chữ],[Kiểu chữ]),bg=[màu nền],fg=[màu chữ])
Ex: lb_1=Label(root,text="Họ và tên:", font=("cambria",12, "bold"))
'''

lb_1=Label(root, text="Họ và tên:", font=("cambria",12))
lb_1.grid(column = 0, row = 0)
lb_2=Label(root, text="Giới tính", font=("cambria",12))
lb_2.place(x=0, y=30) #x=column, y=row ; #lb_2.grid(column = 20, row = 10)

'''
3. Làm việc với Textbox
- Tạo textbox: [Tên texbox]=Entry([Tên cửa sổ],width=[độ rộng],bd=[độ dày viền])
- Lấy dữ liệu từ textbox: [Tên texbox].get()
- Đặt texbox tại vị trí (x,y): [Tên texbox].place(x=[cột],y=[hàng])
'''
txt_tb=Entry(root, text="Lập trình Python", width=20, border=1)
txt_tb.place(x=100, y=0)

#—————————————Combobox————————————
gioi_tinh = StringVar()
gioi_tinh.set("one")
genders=("Nam","Nữ","Khác")
cbo_gioi_tinh=Combobox(root, values=genders)
cbo_gioi_tinh.place(x=100, y=30)

#—————————————Listbox————————————-
days_in_week=("Mon", "Tue", "Web", "Thu", "Fri", "Sat", "Sun")
list_1=Listbox(root, height=5, selectmode='multiple')
for day in days_in_week:
    list_1.insert(END, day)
    list_1.place(x=100, y=55)
    
#————————————–Radiobutton———————————–
rv=IntVar()
rv.set(1)
rdo1=Radiobutton(root, text="Giáo viên", variable=rv, value=1)
rdo2=Radiobutton(root, text="Học sinh", variable=rv, value=2)
rdo1.place(x=250, y=0)
rdo2.place(x=350, y=0)

#————————————-Checkbutton———————————–
cv1 = IntVar()
cv2 = IntVar()
chk1 = Checkbutton(root, text = "Âm nhạc", variable = cv1)
chk2 = Checkbutton(root, text = "Thể thao", variable = cv2)
chk1.place(x=250, y=30)
chk2.place(x=350, y=30)

'''——————————–Msgbox——————————————
* messagebox
    .showinfo("Tiêu đề","Nội dung thông báo")
    .showwarning("Tiêu đề","Nội dung cảnh báo")
    .showerror("Tiêu đề","Nội dung báo lỗi"))
res=messagebox.askquestion("Thông báo","Yêu cầu lựa chọn Yes/No")
res=messagebox.askyesno("Thông báo","Yêu cầu lựa chọn Yes/No")
res=messagebox.askyesnocancel("Thông báo","Yêu cầu lựa chọn Yes/No/Cancel")
res=messagebox.askretrycancel("Thông báo","Yêu cầu lựa chọn Retry/Cancel")
* Giá trị của:
    + res=True (ứng với Yes, Ok, Retry)
    + res=False (ứng với No, Cancel)
    + Với .askyesnocancel: res=True, False, None (ứng với Yes, No, Cancel)
'''
#res=messagebox.askquestion("Thông báo","Yêu cầu lựa chọn Yes/No")
#res=messagebox.askyesno("Thông báo","Yêu cầu lựa chọn Yes/No")
#res=messagebox.askretrycancel("Thông báo","Yêu cầu lựa chọn Retry/Cancel")
#———————————————————————————-
res=messagebox.askyesnocancel("Thông báo", "Yêu cầu lựa chọn Yes/No/Cancel")
if(res==True):
    print("Yes clicked!")
if(res==False):
    print("No clicked!")
if(res==None):
    print("Cancel clicked!")
#———————————————————————————-
''' 1. Khai báo nút bấm (Button)
+ [Tên nút bấm] = Button([Tên cửa sổ],text=[Nội dung hiển thị],bf=[màu nền], fg=[màu chữ])
+ Xử lý sự kiện nút bấm: Thực hiện 1 chương trình con def
def [tên sự kiện]():
[Câu lệnh]
* Gắn sự kiện cho nút bấm
[Tên nút bấm]=Button([Tên cửa sổ],text=[Nội dung hiển thị],command=[Tên sự kiện])
'''

def cmd_yes():
    messagebox.showinfo("Thông báo", "Cảm ơn bạn đã đăng ký!")

cmbt1=Button(
    root, text="Đăng ký",font=("consolas", 10),
    bg="yellow",fg="red",
    command=cmd_yes
) # bf=[màu nền], fg=[màu chữ]
cmbt1.place(x=5, y=60)

''' Scrolledtext //gọi tắt scrtxt
[tên scrtxt]=scrolledtext.ScrolledText([Tên cửa sổ],width=x,height=y)
[tên scrtxt]
    .insert(INSERT,[Nội dung chèn vào scrtxt])
    .delete(1.0,END) //xóa nội dung trong scrtxt
'''
scrtxt=scrolledtext.ScrolledText(root, width=20, height=5)
scrtxt.place(x=250,y=55)
scrtxt.insert(INSERT,"Lập trình Python\n")
scrtxt.insert(INSERT,"Lập trình PHP\n")
scrtxt.insert(INSERT,"Lập trình C#\n")


root.mainloop()