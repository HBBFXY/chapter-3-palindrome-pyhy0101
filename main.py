input_str = input("请输入一个5位数字：")
if len(input_str) != 5:
    print("错误提示：输入不是5位数字")
else:
    # 检查是否为纯数字
    if not input_str.isdigit():
        print("错误提示：输入包含非数字字符")
    else:
        # 判断是否为回文数
        if input_str == input_str[::-1]:
            print("是回文数")
        else:
            print("不是回文数")
