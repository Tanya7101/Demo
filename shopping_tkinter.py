import json
from tkinter import *
from tkinter.font import families
import tkinter.messagebox

membersjson = open("members.json", encoding = 'utf8')
members_f = json.loads(membersjson.read())

Login_name = 'acc'
Login_pasw = 123
class mainwindow(): 
    def __init__(self, master):
        self.master = master
        self.master.geometry = ('800x500')
        self.master.title('main')

        self.bt1 = Button(self.master, text="LOGIN", command=self.bt1_event).grid(column=0, row=5)
        self.lab1 = Label(self.master, text='歡迎進入系統').grid(column=6, row=2)
        self.menu = Menu(self.master)
        self.menulist1 = Menu(self.menu)
        self.menu.add_cascade(label='選單', menu=self.menulist1)
        self.menulist1.add_command(label="申辦會員", command=self.create_mem)
        self.menulist1.add_command(label='Exit', command=self.menu_exit)
        self.master.config(menu=self.menu)


    def bt1_event(self):
        root2 = Toplevel(self.master)
        winlogin = Login(root2)

    def menu_exit(self):
        self.master.destroy()
    
    def create_mem(self):
        root3 = Toplevel(self.master)
        wincreate = Create(root3)

class Login():
    def __init__(self, master):
        self.master = master
        self.master.geometry = ('800x500')
        self.master.title('login')
        
        self.labname = Label(self.master, text='帳號').grid(column=0, row=0)        
        self.labpasw = Label(self.master, text='密碼').grid(column=0, row=1)
        self.txtname = StringVar()
        self.txtpasw = StringVar()
        self.txtname_box = Entry(self.master, textvariable=self.txtname).grid(column=1, row=0)
        self.txtpasw_box = Entry(self.master, textvariable=self.txtpasw).grid(column=1, row=1)
        self.bt2 = Button(self.master, text='登入', command=self.bt2_event).grid(column=2,row=2)
    def bt2_event(self):
        global Login_name 
        global Login_pasw
        Login_name = self.txtname.get()
        Login_pasw = self.txtpasw.get()
        for member_i in range(len(members_f)):
            if Login_name == members_f[member_i]["logname"]:
                if Login_pasw == members_f[member_i]["logpswd"]:
                    tkinter.messagebox.showinfo('login', '歡迎{}登入成功'.format(Login_name))
                    self.master.destroy()
                else:
                    tkinter.messagebox.showerror('loginerr', '密碼錯誤')
            else:
                base = True
            return self.check(base)
    def check(self, base):
        if base:
            tkinter.messagebox.showerror('loginerr', '帳號錯誤')

class Create():
    def __init__(self, master):
        self.master = master
        self.master.geometry = ('800x500')
        self.master.title('create')

        self.lab1 = Label(self.master, text="身分")
        self.lab1.grid(column=0, row=0)
        idlist = ["店家", "會員"]
        self.var_id = StringVar()
        self.menu1 = OptionMenu(self.master, self.var_id, *idlist)
        self.menu1.grid(column=1, row=0)
        self.lab2 = Label(self.master, text="帳號")
        self.lab2.grid(column=0, row=1)
        self.var_usr_name = StringVar()
        self.ent1 = Entry(self.master, textvariable=self.var_usr_name)
        self.ent1.grid(column=1, row=1)
        self.bt1 = Button(self.master, text='確認', command=self.bt1_event)
        self.bt1.grid(column=2, row=1)

    def bt1_event(self):
        self.usr_name = self.var_usr_name.get()
        base = False
        for member_i in range(len(members_f)):
            if members_f[member_i]["logname"] == self.usr_name:
                base = True
            else:
                continue
        return self.createinformationerr(base)
    def createinformationerr(self, base):
        if base:
            tkinter.messagebox.showerror('error', "重複帳號")
        else:
            tkinter.messagebox.showinfo('error', "無此帳號，可創建")
            return self.uname_creat()

    def uname_creat(self):
        #密碼
        self.lab3 = Label(self.master, text="密碼")
        self.lab3.grid(column=0, row=2)
        self.var_usr_pasd = StringVar()
        self.ent3 = Entry(self.master, textvariable=self.var_usr_pasd)
        self.ent3.grid(column=1, row=2)
        #姓名
        self.lab4 = Label(self.master, text="名稱")
        self.lab4.grid(column=0, row=3)
        self.var_rel_name = StringVar()
        self.ent4 = Entry(self.master, textvariable=self.var_rel_name)
        self.ent4.grid(column=1, row=3)
        #電話
        self.lab5 = Label(self.master, text="電話")
        self.lab5.grid(column=0, row=4)
        self.var_ph_name = StringVar()
        self.ent5 = Entry(self.master, textvariable=self.var_ph_name)
        self.ent5.grid(column=1, row=4)
        #地址
        self.lab6 = Label(self.master, text="地址")
        self.lab6.grid(column=0, row=5)
        self.var_add_name = StringVar()
        self.ent6 = Entry(self.master, textvariable=self.var_add_name)
        self.ent6.grid(column=1, row=5)
        
        self.bt2 = Button(self.master, text='創建', command=self.bt2_event)
        self.bt2.grid(column=1, row=6)
    
    def bt2_event(self):
        l = len(members_f)+1
        if self.var_id.get() != "":
            identity = self.var_id.get()
            if self.var_usr_name.get():
                usr_name = self.var_usr_name.get()
                if self.var_usr_pasd.get() != "":
                    usr_pasw = self.var_usr_pasd.get()
                    if self.var_rel_name.get() != "":
                        usr_realname = self.var_rel_name.get()
                        if self.var_ph_name.get() != "":
                            usr_phone = self.var_ph_name.get()
                            if self.var_add_name.get() != "":
                                usr_address = self.var_add_name.get()
                                with open('members.json',"w") as fp:
                                    members_f.append({'seq': l , 'id': identity, 'username': usr_realname, 'logname': usr_name, 'logpswd': usr_pasw, 'phone': usr_phone, 'address': usr_address})
                                    json.dump(members_f, fp)
                                self.master.destroy()
                            else:
                                tkinter.messagebox.showerror('error', '未輸入地址')
                        else:
                            tkinter.messagebox.showerror('error', '未輸入電話')
                    else:
                        tkinter.messagebox.showerror('error', '未輸入姓名')
                else:
                    tkinter.messagebox.showerror('error', '未填密碼')
            else:
                tkinter.messagebox.showerror('error', '未輸入帳號')
        else:
            tkinter.messagebox.showerror('error', '未選擇身分')

def main():
    root = Tk()
    mywindow = mainwindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()