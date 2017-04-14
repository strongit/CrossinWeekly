# Crossin 2017/04/07


def pingpong(n, k=7, step=1):
    pingpong_list = [1]
    try:
        for i in range(1, n+1):  # 和下面的打印列表倒数第二个数一起，可以处理负数和0的输入
            step *= (i % k == 0 or str(k) in str(i))*-2+1
            pingpong_list.append(pingpong_list[-1] + step)
        print(pingpong_list[-2])
    except:
        print('input error')
    return 0


if __name__ == '__main__':
    pingpong(7, 7)
    pingpong(8, 8)
    pingpong(55, 6)
    pingpong(100, 9)
