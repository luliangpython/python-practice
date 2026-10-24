print("简单计算器")
print("支持：+ - * /")

a = float(input("请输入第一个数："))
op = input("请输入运算符：")
b = float(input("请输入第二个数："))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        print("错误：不能除以0")
    else:
        result = a / b
else:
    print("不支持的运算符")

if "result" in dir():
    print("结果：", result)