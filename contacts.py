contacts = []
while True:
    print("""1="添加联系人"
2="查看所有联系人"
3=“退出”""")
    a=int(input("选一个："))
    if a==1:
        name=input("姓名：")
        phone=input("电话：")
        dic={"name":name,"phone":phone}
        contacts.append(dic)
        print("添加成功")
    elif a==2:
        for x in contacts:
            print(x["name"],x["phone"])
    else:
        print("再见")
        break


