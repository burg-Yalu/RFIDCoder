import random


def XOR(str1, str2):  # 实现模2减法
    ans = ''
    if str1[0] == '0':
        return '0', str1[1:]
    else:
        for i in range(len(str1)):
            if (str1[i] == '0' and str2[i] == '0'):
                ans = ans + '0'
            elif (str1[i] == '1' and str2[i] == '1'):
                ans = ans + '0'
            else:
                ans = ans + '1'
    return '1', ans[1:]


def CRC_Encoding(str1, str2):  # CRC编码
    length = len(str2)
    str3 = str1 + '0' * (length - 1)
    ans = ''
    yus = str3[0:length]
    for i in range(len(str1)):
        str4, yus = XOR(yus, str2)
        ans = ans + str4
        if i == len(str1) - 1:
            break
        else:
            yus = yus + str3[i + length]
    ans = str1 + yus
    return ans


def CRC_Decoding(str1, str2):  # CRC解码
    length = len(str2)
    str3 = str1 + '0' * (length - 1)
    yus = str3[0:length]
    for i in range(len(str1)):
        str4, yus = XOR(yus, str2)
        if i == len(str1) - 1:
            break
        else:
            yus = yus + str3[i + length]
    return yus == '0' * len(yus)


def generate_binary_data(num_bits=8):  # 生成随机二进制数据（8位）
    return ''.join(random.choice('01') for _ in range(num_bits))


def main():  # 主函数
    # 生成100组8位二进制数据并存储在一个数组中
    binary_data_list = [generate_binary_data() for _ in range(100)]

    # 用户输入生成比特模式
    str2 = input("请输入生成比特模式：")

    # 模拟发送这些数据并通过CRC编码
    encoded_data_list = []
    for str1 in binary_data_list:
        encoded_data = CRC_Encoding(str1, str2)
        encoded_data_list.append(encoded_data)
        print(f"原始数据: {str1}, 编码后数据: {encoded_data}")

    # 验证编码数据
    for i, encoded_data in enumerate(encoded_data_list):
        flag = CRC_Decoding(encoded_data, str2)
        if flag:
            print(f"数据 {i + 1} 验证完成，未出错")
        else:
            print(f"数据 {i + 1} 验证失败，出错")

    # 提供退出选项
    while True:
        print('==' * 30)
        setting = input("请输入运行模式（0：退出，1：CRC编码，2：CRC验证）：")
        if setting == '0':
            break
        elif setting == '1':
            str1 = input("请输入数据：")
            str2 = input("请输入生成比特模式：")
            str3 = CRC_Encoding(str1, str2)
            print("{} 编码后为: {}".format(str1, str3))
        elif setting == '2':
            str1 = input("请输入验证数据：")
            str2 = input("请输入生成比特模式：")
            flag = CRC_Decoding(str1, str2)
            if flag:
                print("验证完成，未出错")
            else:
                print("sorry 验证数据已出错")
        else:
            print("请正确输入：")


main()
