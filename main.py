# 这里编写你的代码
def main():
    # 获取用户输入
    num_str = input("")
    # 检查输入是否为5位且全部是数字
    if len(num_str) != 5 or not num_str.isdigit():
        print("输入错误: 请输入5位数字")
        return
    # 判断是否为回文数
    if num_str == num_str[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
if __name__ == "__main__":
    main()
