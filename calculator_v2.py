print("简单计算器")
print("支持：+ - * /")
last = None
re = "y"

while re == "y":
    if last is None:
        a = float(input("第一个数："))
    else:
        a = last
        print("用上次的：", a)
        
    op = input("请输入运算符：")
    b = float(input("第二个数："))
    
    if op == "+":
        result = a + b
        print("结果：", result)
        last = result
    elif op == "-":
        result = a - b
        print("结果：", result)
        last = result
    elif op == "*":
        result = a * b
        print("结果：", result)
        last = result
    elif op == "/":
        if b == 0:
            print("错误：不能除以0")
        else:
            result = a / b
            print("结果：", result)
            last = result
    else:
        print("输入了错误的运算符")
        
    re = input("继续吗？(y/n)：")

print("再见")






