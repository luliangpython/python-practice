dict={"张三": 85, "李四": 92, "王五": 78}
a=input("请输入名字：")
if a in dict:
    print(a+"的分数是："+str(dict[a]))
else:
    print("查无此人")
