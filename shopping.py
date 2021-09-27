#基礎設定值
import json
membersjson = open("members.json", encoding = 'utf8')
menujson = open("menu.json", encoding = 'utf8')
cartjson = open("cart.json", encoding = 'utf8')
members_f = json.loads(membersjson.read())
menu_f = json.loads(menujson.read())
cart_f = json.loads(cartjson.read())
l = len(members_f)+1
m = len(menu_f)+1
c = len(cart_f)+1
car = []
total = []
#主程式架構
def check(realname):
    for menu_i in range(len(menu_f)):
        if menu_f[menu_i]["username"] == realname:
            print(menu_f[menu_i]["item"],menu_f[menu_i]["price"])
    return shop(realname)
def out(realname):
    delect = str(input("請輸入欲刪除菜單品項(結束新增請打q):"))
    for menu_i in range(len(menu_f)):
        if delect == 'q' or delect == 'Q':
            return shop(realname)
        elif menu_f[menu_i]["item"] == delect:#還沒刪
            print("已刪除",delect)
            return out(realname)
        else:
            print("無此品項")
            return out(realname)
def add(realname):
    produce = str(input("請輸入欲新增菜單品項(結束新增請打q):"))
    for menu_i in range(len(menu_f)):
        if produce == 'q' or produce =='Q':
            return shop(realname)
        elif menu_f[menu_i]["item"] != produce :
            price = int(input("請輸入新增項目價格:"))
            with open('menu.json',"w") as pr:
                menu_f.append({"seq": m, "username": realname, "item": produce, "price": price})
                json.dump(menu_f, pr)
            return add(realname)
        elif menu_f[menu_i]["item"] == produce:
            print("已有重複品項")
            return add(realname)
def shop(realname):
    do = str(input("請輸入欲執行項目(新增、刪除、查看、結束):"))
    if do == "新增":
        return add(realname)
    elif do == "刪除":
        return out(realname)
    elif do == "查看":
        return check(realname)
    elif do == "結束":
        print("登出本系統")
    else:
        print("輸入錯誤")
        return shop(realname)
def allmenu(realname):
    print("菜單價格")
    for menu_i in range(len(menu_f)):
        print(menu_f[menu_i]["item"], menu_f[menu_i]["price"])
    return memberlogin(realname)
def memberlogin(realname):
    msg = str(input("請點餐(若有需要重新查看菜單請輸入查看，結束點餐請打q):"))
    if msg == "查看":
        return allmenu(realname)
    elif msg == "q" or msg =="Q":
        if not car:
            print("未點餐")
        else:
            print("結束點餐，已點",car)
            money = sum(total)
            print("總金額為",money)
            with open('cart.json',"w") as ca:
                cart_f.append({'seq': c , 'username': realname, "cart": car, "money": money})
                json.dump(cart_f, ca)
            total.clear()
            car.clear()
    else:
        t=False
        for menu_i in range(len(menu_f)):
            if msg == menu_f[menu_i]["item"]:
                sq=menu_i
                t=True
            else:
                continue
        if t == True:
            car.append(menu_f[sq]["item"])
            total.append(int(menu_f[sq]["price"]))
        else:
            print("無此品項")
        return memberlogin(realname)
def creat(): #若帳號密碼與店家或會員資料完全吻合，則詢問是否有本網站會員
    print("為您創建資料")
    identity = str(input("請輸入身分(店家/會員):"))
    if identity == "店家" or identity == "會員":
        uname = str(input("請輸入創建帳號名:"))
        pasw = str(input("請輸入密碼:"))
        for log_i in range(len(members_f)):
                if members_f[log_i]["logname"] == uname:
                    print("已有重複帳號")
                    return creat()
                else:
                    realname = str(input("請輸入店名："))
                    address = str(input("請輸入地址："))
                    phone = str(input("請輸入電話："))
                    if identity == '店家':
                        with open('members.json',"w") as fp:
                            members_f.append({'seq': l , 'id': '店家', 'username': realname, 'logname': uname, 'logpswd': pasw, 'phone': phone, 'address': address})
                            json.dump(members_f, fp)
                    elif identity == '會員':
                        with open('members.json',"w") as fp:
                            members_f.append({'seq': l , 'id': "會員", 'username': realname, 'logname': uname, 'logpswd': pasw, 'phone': phone, 'address': address})
                            json.dump(members_f, fp)
    else:
        print("輸入錯誤")
        return creat()
def login(realname):
    for log_i in range(len(members_f)):
        if members_f[log_i]["username"] == realname:
            if members_f[log_i]["id"] == "店家":
                choose = str(input("請選擇登入系統(餐點修改系統請打1，會員點餐系統請輸2)："))
                if choose == "1":
                    return shop(realname)
                elif choose == "2":
                    print("歡迎{}進入點餐系統".format(realname))
                    return allmenu(realname)
                else:
                    print("輸入錯誤，重新登入")
                    return login(realname)
            else:
                print("歡迎{}進入點餐系統".format(realname))
                return allmenu(realname)
def log():
    logname = str(input("請輸入帳號:"))
    logpasw = str(input("請輸入密碼:"))
    for log_i in range(len(members_f)):
        if members_f[log_i]["logname"] == logname: #會員登入
            realname = members_f[log_i]["username"]
            return login(realname)
        else:
            print("無此帳號")
            break
def main(a):
    print("歡迎進入點餐系統")
    while True:
        a = str(input("是否為本網站會員(請輸入y/n):"))
        if a == 'y' or a == 'Y':
            log()
        elif a == 'n' or a == 'N':
            creat()
        else:
            print("輸入錯誤，請重新輸入")
    return 0
#登入問題、刪除資料問題--未做