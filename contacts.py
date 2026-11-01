contacts = []
while True:
    print("""1="添加联系人"
2="查看所有联系人"
3=“搜索联系人”
4=“删除联系人”
5=“修改联系人”
6=“退出”""")
    a=input("选一个：")
    if a=="1":
        name=input("姓名：")
        phone=input("电话：")
        dic={"name":name,"phone":phone}
        contacts.append(dic)
        print("添加成功")
    elif a=="2":
        for x in contacts:
            print(x["name"],x["phone"])
    elif a=="3":
        b=input("请输入姓名：")
        for x in contacts:
            if b==x["name"]:
                print(x["name"],x["phone"])
                break
        else:
            print("未查找到联系人")
    elif a=="4":
        c=input("要删除的姓名：")
        for x in contacts:
            if c==x["name"]:
                contacts.remove(x)
                print("删除成功")
                break
        else:
            print("用户不存在")
    elif a=="5":
        d=input("请输入姓名")
        for x in contacts:
            if d==x["name"]:
                e=input("请输入新名字：")
                f=input("请输入新电话号码：")
                x["name"]=e  
                x["phone"]=f
                print("修改成功")
                break
        else:
            print("用户不存在")
    elif a=="6":
        print("再见")
    else:
        print("选项无效")

