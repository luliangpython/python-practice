import random

secret = random.randint(1, 100)
print("我想到一个1~100的数，你猜猜看")
count=0
while True:
    count=count+1
    a=int(input("请输入你猜的数字："))
    if a==secret:
        print("对了,猜了{}次".format(count))
        break
    elif a<secret:
        print("小了")
    else:
        print("大了")
